# -*- coding: utf-8 -*-
from setting import config
import os
import numpy as np
import cv2
from preprocessing.hand_detect import get_coordinate, make_model



def prepocess_data(height=224, width=224, channel=3, get_npy=True, get_images=False):
    #model set
    weights = os.path.join(config.PATH_MODEL,'cross-hands.weights')
    cfg = os.path.join(config.PATH_MODEL,'cross-hands.cfg')
    net, output_layers = make_model(weights,cfg)

    #path of raw_data 
    RAW_DATA = config.get_data_path('raw_data')
    
    #label list
    label_lst = [label for label in os.listdir(RAW_DATA)]

    #create ndarray as default
    if get_npy:
        data_array = np.empty((0,height,width,channel))
        y_lst = []
        y_temp = 0

    for label in label_lst:
        #label_path which contains videos
        label_path = os.path.join(RAW_DATA, label)
        
        #create folder for images when 'get_images=True'
        if get_images:
            folder_name = os.path.join(config.PATH_DATA,label)
            try: 
                # create a folder 
                if not os.path.exists(folder_name): os.makedirs(folder_name) 
        
            # if not created then raise error 
            except OSError: print ('can not create folder')
        
        #set path for each videos
        for video in os.listdir(os.path.join(RAW_DATA, label)):
            video_path = os.path.join(label_path, video)

            #read video
            cam = cv2.VideoCapture(video_path)

            #start frame
            currentframe = 0

            while True:
                #read from frame
                ret, frame = cam.read()
                
                #if frame still left
                if ret:
                    hand_area = get_coordinate(320,frame, net,output_layers)
                    
                    #when hand area not detected
                    if not hand_area: continue

                    #slice hand area and resize
                    hand_x, hand_y, w, h = hand_area
                    hand_slice = frame[round(hand_y*0.9):round((hand_y+h)*1.1), round(hand_x*0.9):round((hand_x+w)*1.1)]
                    resized_frame = cv2.resize(hand_slice, (width, height), interpolation=cv2.INTER_CUBIC)
                    
                    #append data at ndarray as default
                    if get_npy:
                        data_array = np.append(
                            data_array, resized_frame.reshape((1,height,width,channel)), axis=0
                        )
                    
                    # write image when 'get_images=True'
                    if get_images:
                        head = os.path.join(folder_name,video[-7:-4])
                        name = f'{head}_{currentframe:0>5}.jpg'
                        cv2.imwrite(name, resized_frame)
                    currentframe += 1
                    y_temp += 1
                else: break
                
            cam.release() 
            cv2.destroyAllWindows() 

        if get_npy:    
            y_lst.append(y_temp)
            y_temp = 0
    if get_npy: 
        #save X_data
        np.save(f'{os.path.join(config.PATH_DATA,"X_data")}',data_array)
        
        #create target data and save
        Y = np.empty((0,len(y_lst)),dtype=int)
        for i in range(len(y_lst)):
            temp = [0] * len(y_lst)
            temp[i] = 1
            for j in range(y_lst[i]):
                y_temp = np.reshape(temp,(1, len(y_lst)))
                Y = np.append(Y,y_temp,axis=0)
        np.save(f'{os.path.join(config.PATH_DATA,"Y_data")}',Y)

if __name__ == '__main__':
    prepocess_data(width=400,height=300,get_images=True)
 


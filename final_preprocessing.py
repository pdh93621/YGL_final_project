from preprocessing.hand_detect import get_coordinate
import cv2
import numpy as np
from setting import config
import os

class Preprocessing:
    models = ['cross-hands','cross-hands-tiny-prn','cross-hands-yolov4-tiny']
    
    def __init__(self, model_select, save = 0, data_for = 'train'):        
        self.model_select = model_select
        self.weights = os.path.join(config.PATH_MODEL,f'{Preprocessing.models[self.model_select]}.weights')
        self.cfg = os.path.join(config.PATH_MODEL,f'{Preprocessing.models[self.model_select]}.cfg')
        self.x = None
        self.y = None
        self.w = None
        self.h = None
        self.save = save
        self.find_coordinate = False
        self.data_for = data_for
        self.make_model() 

    def make_model(self):
        self.net = cv2.dnn.readNet(self.weights, self.cfg)       
        layer_names = self.net.getLayerNames()
        self.output_layers = [layer_names[i[0]-1] for i in self.net.getUnconnectedOutLayers()]

    def get_coordinate(self, img, size = 320, select_boxes = 'only'):
        height, width, _ = img.shape
        blob = cv2.dnn.blobFromImage(img, 0.00392, (size,size), (0,0,0), True, crop=False)
        outs = self.net.setInput(blob)

        boxes = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    if select_boxes == 'only':
                        self.x, self.y, self.w, self.h = x, y, w, h
                        box = [x,y,w,h]
                        return box
                    elif select_boxes == 'all':
                        boxes.append([x,y,w,h])
        if len(boxes):
            self.x = [box[0] for box in boxes]
            self.y = [box[1] for box in boxes]
            self.w = [box[2] for box in boxes]
            self.h = [box[3] for box in boxes]
            return boxes
        else:
            False
        
    def add_rectangle(self, img, color):
        cv2.rectangle(img, (self.x, self.y), (self.x+self.w,self.y+self.h), color, 3)
        if self.save:
            cv2.imwrite('rectangled_img.jpg', img)

    def slice_image(self, img):
        sliced_img = img[self.y:self.y + self.h, self.x: self.x + self.w]
        if self.save:
            cv2.imwrite('sliced_img.jpg', sliced_img)
        return sliced_img

    def get_data(self, video_path = 0):
        train = []
        cap = cv2.VideoCapture(video_path)
        while True:
            ret, frame = cap.read()
            if frame is None:
                break
            if ret:
                if self.find_coordinate:
                    color = (0,255,0)
                    sliced_img = self.slice_image(frame)
                    self.add_rectangle(frame, color)                    
                    if self.data_for == 'train':
                        np.append(train, sliced_img.reshape(1,self.h,self.w,3),axis=0)
                    elif self.data_for == 'test':
                        return sliced_img
                else:
                    if self.get_coordinate(img = frame):
                        self.find_coordinate = True
                        train = np.empty((0,self.h,self.w,3))
        return train
import os

class SetEnvironment:
    availables = ['pdf','potx','pptx','ppt','ppsx','show']
    def __init__(self):
        self.exe_path = None
        self.ppt_path = None

    def get_exepath(self):
        exe_path = input()
        if exe_path.split('.')[-1] != 'exe':
            return False
        self.exe_path = exe_path
        return True
    
    def get_pptpath(self):
        ppt_path = input()
        if ppt_path.split('.')[-1] not in Environment.availables:
            return False
        self.ppt_path = ppt_path
        return True
    
    def check(self):
        if self.exe_path != None and self.ppt_path != None:
            try:            
                batch_ppt = 'start' + ' "'+ self.exe_path + '" ' + self.ppt_path
                os.system(batch_ppt)
                return True
            except:
                return False 
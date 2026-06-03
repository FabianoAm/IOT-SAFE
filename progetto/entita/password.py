class Password:
    def __init__(self):
        self.p=[]
        self.password=[]
        
    def set_password(self):
        if len(self.p)==4:
            self.password=self.p
            return True
        return False
        
    def is_correct(self):
        if len(self.password)==4 and self.password==self.p:
            return True
        else:
            return False
    def is_not_correct(self):
        if len(self.password)==4 and len(self.p)==4 and self.password!=self.p:
            return True
        else:
            return False
        
    def reset(self):
        self.password=[]
        
        
    def is_null(self):
        if len(self.password)==0:
            return True
        else:
            return False
        
    def append(self,n):
        self.p.append(n)
        
    def len_p(self):
        return len(self.p)
    
    def clear(self):
        self.p=[]
        
    def get_password(self):
        return self.password
    
    def mqtt_c(self, msg):
        self.password = list(msg)
        
    def get_p(self):
        return self.p
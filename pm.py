import datetime

class pm:
    def __init__(self):
        self.dt1 = datetime.datetime.now()
        self.dt2 = self.dt1

    def __str__(self):
        if self.dt1 >= self.dt2:
            self.dt2 = datetime.datetime.now()
        return str(self.delta())

    def start(self):  
        self.dt1 = datetime.datetime.now()

    def stop(self):
        self.dt2 = datetime.datetime.now()
        return self
        
    def delta(self):
        return self.dt2 - self.dt1

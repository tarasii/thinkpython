import datetime

class pm:
    def __init__(self):
        self.dt1 = datetime.datetime.now()
        self.dt2 = self.dt1
        self.dt3 = self.dt1

    def __str__(self):
        return "{}: {}".format(self.dt2, str(self.delta()))
        
    def delta(self, type=0):
        if type == 0:
            return self.dt2 - self.dt1
        else:
            return self.dt2 - self.dt3

    def reset(self):
        self.dt3 = self.dt2
        self.dt2 = datetime.datetime.now()

    def msg(self, txt=""):
        print txt, self.dt2, self.delta(), self.delta(1)

    def cnt(self, txt=""):
        self.reset()
        self.msg(txt)

class Glass:
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0

    def pour_in(self, amount):
        if ((self.amount + amount)>self.capacity):
            self.amount = self.capacity
        else:
            self.amount = self.amount + amount 

    def pour_out(self, amount):
        if ((self.amount - amount)<0):
            self.amount = 0
        else:
            self.amount = self.amount - amount 
 
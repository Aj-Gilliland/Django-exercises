class BalloonTooFull(Exception):
    pass


class Balloon:
    def pump(self):
        self.amount += 3
        if self.amount > self.capacity:
            raise BalloonTooFull("Pop!")

    def release(self):
        self.amount -= 2
        self.amount = max(0, self.amount)

class SwordBalloon(Balloon):
    def __init__(self):
        self.capacity = 5
        self.amount = 0

    pump = Balloon.pump
    release = Balloon.release

class DogBalloon(Balloon):
    def __init__(self):
        self.capacity = 7
        self.amount = 0

    pump = Balloon.pump
    release = Balloon.release

class TriforceBalloon(Balloon):
    def __init__(self):
        self.capacity = 11
        self.amount = 0

    pump = Balloon.pump
    release = Balloon.release

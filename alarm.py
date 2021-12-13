class Alarm:
    def __init__(self):
        self.active = False
        self.ringing = False

    def activate(self):
        if self.active:
            raise Exception('alarm is already active')

        self.active = True

    def deactivate(self):
        if not self.active:
            raise Exception('alarm is already inactive')

        self.active = False
        self.ringing = False
    
    def reset(self):
        if not self.ringing:
            raise Exception('alarm is not ringing')

        self.ringing = False
    
    def motionDetected(self):
        if self.active:
            self.ringing = True
    
    def isActive(self):
        return self.active
    
    def isRinging(self):
        return self.ringing
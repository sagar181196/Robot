class Battery:
    battery = 100

    def battery_low(self,battery):
        if battery<10:
            print("battery is lower than 10")

    def battery_validator(self,battery):
        if battery>2:
            print('Battery consumption must not be greater than 2 ')

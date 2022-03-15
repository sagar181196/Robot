class battery:
    def __init__(self,left):
        self.left=left

    def battery_low(self,battery):
        if battery<10:
            print("battery is lower than 10")

    def battery_validator(self,battery):
        if battery>2:
            print('not valid')




print('Enter the battery consumption ')


left= input('1.left: ')
right = input('2.Right :')
up = input('3.Upward : ')
down = input('4.Downward : ')

bb=battery(left,right)
bb.battery_validator()


# Improve It



# print('battery left={}'.format(100-battery))
from moves import Motion
from battery import Battery


class Robot(Motion,Battery):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def boundaries(self,moves,times):
        ro_x,ro_y=self.robot_motion(moves,times)
        self.print_motion()
        if ro_x<0 or ro_x>self.length:
            print('out of boundary')
        elif ro_y<0 or ro_x>self.breadth:
            print('out of boundary')

    def battery_consumption(self,left,right,up,down,times,move):
        if move =='L':
            battery=left*times
        elif move == 'R':
            battery=right*times
        elif move=='U':
            battery=up*times
        elif move=='D':
            battery=down*times
        battery =  100-battery
        self.battery_low(battery)
        return battery



length=int(input('length: '))
breadth= int(input('breadth: '))

rb = Robot(length,breadth) 

print('Enter the battery consumption ')

left= int(input('1.left: '))
rb.battery_validator(left)

right = int(input('2.Right :'))
rb.battery_validator(right)

up = int(input('3.Upward : '))
rb.battery_validator(up)

down = int(input('4.Downward : '))
rb.battery_validator(down)   



move, times= input('Move, Times:').split()
move = move.upper()
times = int(times) 

rb.boundaries(move,times)  

move, times= input('Move, Times:').split()
move = move.upper()
times = int(times) 
rb.boundaries(move,times)  


move, times= input('Move, Times:').split()
move = move.upper()
times = int(times) 
rb.boundaries(move,times)  


move, times= input('Move, Times:').split()
move = move.upper()
times = int(times) 
bb=rb.battery_consumption(left,right,up,down,times,move)
print('battery: ',bb)


rb.move_validaion(move)
rb.boundaries(move,times)      

rb.instruction(move)
rb.reset()



   














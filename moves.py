class Motion:
    x =0
    y=0

    def move_validaion(self,move):
        if move != 'L' and move != 'R' and move != 'U' and move != 'D':
            print('Invalid move')

    def robot_motion(self,move,times):
        
        if move =='L':
            self.x = self.x-times
        elif move == 'R':
            self.x = self.x+times 
        elif move == 'U':
            self.y = self.y+times
        elif move == 'D':
            self.y = self.y-times
       
    def print_motion(self):       
        print('your robot move ({0} {1})'.format(self.x,self.y))

move, times= raw_input('Move, Times:').split()
move = move.upper()
times = int(times)

aa=Motion()
aa.move_validaion(move)
aa.robot_motion(move,times)
aa.print_motion()
aa.robot_motion(move,times)
aa.print_motion()
aa.robot_motion(move,times)
aa.print_motion()
# aa.reset()





# battery=aa.robot_motion_battery(times,move)
# Reset it 0,0



class Motion:
    x=0
    y=0
    move_list = []

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
        if self.x==0 and self.y==0:
            print('robot in circular motion')
        return self.x,self.y

       
    def print_motion(self):       
        print('your robot move ({0} {1})'.format(self.x,self.y))


    def reset(self):
        self.x=0
        self.y=0
    
    def instruction(self,move):
        self.move_list.append(move)
        if len(self.move_list) > 4:
            new_list=set(self.move_list[-4:])
            if len(new_list)==1 and new_list.pop()==move:
                print('duplicate entry')
                    





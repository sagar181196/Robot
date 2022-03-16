class Motion:
    x=0
    y=0

    def move_validaion(self,move):
        if move != 'L' and move != 'R' and move != 'U' and move != 'D':
            print('Invalid move')

#     def robot_motion(self,move,times):
        
#         if move =='L':
#             self.x = self.x-times
#         elif move == 'R':
#             self.x = self.x+times 
#         elif move == 'U':
#             self.y = self.y+times
#         elif move == 'D':
#             self.y = self.y-times
       
#     def print_motion(self):       
#         print('your robot move ({0} {1})'.format(self.x,self.y))


#     def reset(self,a):
#         if a=='y':
#             self.x=0
#             self.y=0
#         return self.x,self.y

#     def repeat(self):




move, times= raw_input('Move, Times:').split()
move = move.upper()
times = int(times)

# aa=Motion()
# aa.move_validaion(move)
# aa.robot_motion(move,times)
# aa.print_motion()
# aa.robot_motion(move,times)
# aa.print_motion()
# aa.robot_motion(move,times)
# aa.print_motion()
# # aa.reset()

# a= raw_input('do you want to reset "Y/N" :')
# print(aa.reset(a))


stack=['L','L','L','L']
for i in move:
    stack.append(i)
    if len(stack)>4:
        stack1=set(stack[-4:])
        if len(stack1)==1 and stack1.pop()==move:
            print('repeated move')


# battery=aa.robot_motion_battery(times,move)


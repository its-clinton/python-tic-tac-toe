import os 
from tkinter import messagebox
from tkinter import *
root = Tk()
root.title('tic_tac_toe')

def playgame(a,b):
    global player
    if player == 'M':
        c[a][b].configure(text = 'M')
        player = 'D'
    else:
        c[a][b].configure(text = 'D')
        player = 'M'
   
c = [[0,0,0],
      [0,0,0],
      [0,0,0]] 

for i in range(3):
    for k in range(3):
        c[i][k] = Button(font = ('verdana', 60), width = 3, bg = 'green', command = lambda a=i,b=k: playgame(a,b))
        c[i][k].grid(row = i, column = k)
    
player = 'M'
root.mainloop()
 
        

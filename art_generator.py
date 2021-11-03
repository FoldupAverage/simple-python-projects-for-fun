from turtle import * 
from random import randint 

# Script by: Devendra Kushwah
# https://www.quora.com/Whats-the-coolest-Python-turtle-graphic-you-have-seen

bgcolor('black') 
x = 1 
speed(0) 

while x < 400: 
    r = randint(0,255) 
    g = randint(0,255)  
    b = randint(0,255) 

    colormode(255)  
    pencolor(r,g,b) 
    fd(50 + x) 
    rt(90.991) 
    x = x+1 

exitonclick() 

# Other interesting Ideas on:
# https://discuss.cloudxlab.com/t/fun-with-python-turtle-graphics-module-share-your-turtle-art/4096/7
# def restart():
#     clear()
#     home()
# for i in range(50):
#      circle(100, 360)
#      left(5)

# restart()
# for i in range(100):
#      forward(10+i*5)
#      left(120)

# restart()

# for i in range(200):
#      circle(100, 60-i)
#      left(i)     


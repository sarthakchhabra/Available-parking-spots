import RPi.GPIO as g
import time
g.setmode(g.BCM)
trig=2
echo=3

led1=4
led2=5
led3=6
led4=7
led5=8

g.setup(led1,g.OUT)
g.setup(led2,g.OUT)
g.setup(led3,g.OUT)
g.setup(led4,g.OUT)
g.setup(led5,g.OUT)

g.setup(trig,g.OUT)
g.setup(echo,g.IN)
g.output(trig,0)
time.sleep(2)     //time to settle the sensor
 
while 1:
        g.output(trig,1)
        time.sleep(0.00001)           //trigger provided
        g.output(trig,0)
        while g.input(echo)==0:
                ts=time.time()
        while g.input(echo)==1:       //echo received measured
                te=time.time()
        t=te-ts
        d=17150*t                     //in centimeters
        time.sleep(0.5)
        print(int(d))
        cars=int(d/100)               //each parking space is of 100cm 
        print("no. of cars parked:",cars)
        for i in range(led1,led5+1):
                g.output(i,0)
        if(cars<=5):
                for x in range(1,cars+1):
                        g.output(x+3,1)


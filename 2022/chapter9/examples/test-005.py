import numpy as np
import matplotlib.pyplot as plt

def getFourier(n,x):
    sum=0
    for i in range(1,n+1,2):
            sum+=(1/(i*np.pi))*np.sin(i*x)
    return sum

def draw():
    x= np.linspace(-2*np.pi,2*np.pi,12*1000)
    y=[]
    for i in x:
        value=getFourier(50,i)
        y.append(value)
    y=np.array(y)
    plt.plot(x,y)
    plt.show()

draw()
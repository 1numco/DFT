import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import rfft
import cmath
import math
def DFT(x):
    y=[]
    N=len(x)
    for i in range(len(x)):
        y.append(complex(0,0))
    for k in range(len(x)):
        for n in range(len(x)):
            y[k]+=x[n]*cmath.exp(complex(0,-1*2*math.pi*n*k/len(x)))
        y[k]=abs(y[k])
    for i in range(N//2):
        y[i],y[N//2+i]=y[N//2+i],y[i]
    return y
# def RDFT(y):
#     x=[]
#     for i in range(len(y)):
#         x.append(complex(0,0))
#     for n in range(len(y)):
#         for k in range(len(y)):
#             x[n]+=1/len(y)*y[k]*cmath.exp(complex(0,1*2*math.pi*n*k/len(y)))
#         x[n]=abs(x[n])
#     return x
def file_read():
	my_file = open("input.txt", "r")
	my_string = my_file.read() #first value in the file is sampling interval, and rest is signal values
	my_file.close()
	string_value = my_string.split("\t")
	value=[]
	for i in range(1,len(string_value)):
		value.append(float(string_value[i]))
	delta=float(string_value[0])
	return value,delta


def graph(T,X,Y):
    N=len(X)
    x = np.linspace(0.0, T,N)
    y = np.linspace(-N/(2*T), N/(2*T), N)    
    plt.plot(x,X)
    plt.grid()
    plt.xlabel(u'Time,sec')
    plt.ylabel(u'Amplitude')
    plt.title(u'Graph of signal')
    plt.show()
    plt.plot(y,Y)
    plt.grid()
    plt.xlabel(u'Frequancy, Hz')
    plt.ylabel(u'Power')
    plt.title(u'Graph of the signal spectrum')
    plt.show()
    
    
def main():
    X,T=file_read()
    Y=DFT(X) 
    graph(T,X,Y)
    my_file = open("output.txt", "w")
    my_file.write(str(Y))
    my_file.close()
main()    
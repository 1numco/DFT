import numpy as np
import matplotlib.pyplot as plt
import random
#____________signal generation function, which is the sum of a random number of harmonics with random weights________
def gen():
    rand_freq=random.randint(1,20) 
    max_freq=rand_freq*100   # max frequency in the signal spectrum
    delta=1/(2*max_freq)    # 
    Num=1000     # number of points
    T=Num*delta   # impulse duration
    x=np.linspace(0,T,Num)
    n=random.randint(1,20)
    freq=np.random.randint(1,max_freq/10,n)
    freq=10*freq # these 2 lines are needed to generate frequencies that are at least 10 Hz apart
    weight_coeff=np.random.sample(n)
    print("Number of harmonics:",n,freq)  #for check myself
    sum_arr=np.zeros(Num)
    noise=np.random.sample(1)
    for i in range(n):
        arr=weight_coeff[i]*np.cos(freq[i]*2*np.pi*x)+0.01*noise*np.ones(Num)
        sum_arr+=arr
    return T,sum_arr


#_____________function that writes the resulting sequence of points to a file__________
def write_to_file(T,sum_arr):
    my_file = open("input.txt", "w")
    my_file.write(str(T))
    for i in range(len(sum_arr)):
        my_file.write("\t"+str(sum_arr[i]))
    my_file.close()
    
    
#___________function that draws a graph of the resulting signal______________
def graph(T,sum_arr):
    x=np.linspace(0,T,len(sum_arr))
    plt.plot(x,sum_arr)
    plt.grid()
    plt.show()
    
#_______main_______
T,sum_arr=gen()
graph(T,sum_arr)
write_to_file(T,sum_arr)

#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
from scipy.stats import norm 
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if

maxrange=50
maxlim=6.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1)
randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
randvar = np.loadtxt('codes/tri.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
	

def tri_cdf(x):
	if(x <= 0):
		return 0.0
	elif(x > 0 and x <= 1):
		return (x**2)/2
	elif(x > 1 and x < 2):
		return 1 - ((2-x)**2/2)
	else:
		return 1.0

vec_tri_cdf = np.vectorize(tri_cdf, otypes=[np.float])

plt.plot(x,err,'bo')
plt.plot(x, vec_tri_cdf(x))
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$F_X(x_i)$')
plt.legend(["Simulation", "Analysis"])
#plt.savefig('/home/muskan/Documents/Probability/figs/tri1_cdf.pdf')
#plt.savefig('/home/muskan/Documents/Probability/figs/tri1_cdf.eps')
plt.savefig('/home/muskan/Documents/Probability/figs/tri_cdf.pdf')
plt.savefig('/home/muskan/Documents/Probability/figs/tri_cdf.eps')


#subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#if using termux
#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
plt.show() #opening the plot window
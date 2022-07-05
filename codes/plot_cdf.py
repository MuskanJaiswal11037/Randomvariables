
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
randvar = np.loadtxt('gau.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list
 
 
def Q(x):
     return (1-mp.erf(x/np.sqrt(2)))/2
 
def guass_cdf(x):
     return 1-Q(x)
 
vec_gauss_cdf = np.vectorize(guass_cdf, otypes=[np.float])

rv = norm(0, 1)
plt.plot(x,err,'bo')
plt.plot(x, vec_gauss_cdf(x))
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$F_X(x_i)$')
plt.legend(["Simulation", "Analysis"])
plt.savefig('/home/muskan/Documents/Probability/figs/guass_cdf.pdf')
plt.savefig('/home/muskan/Documents/Probability/figs/guass_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#if using termux
#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
plt.show() #opening the plot window
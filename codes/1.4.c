#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"



int  main(void) //main function begins
{
 double t,p;
//Uniform random numbers
uniform("uni.dat", 1000000);


//Mean of uniform

printf("%lf \n",mean("uni.dat"));
t=mean("uni.dat");
p=(double)var("uni.dat");
 printf("%lf \n",p);

return 0;
}


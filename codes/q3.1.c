#include<stdio.h>
#include<stdlib.h>
#include<math.h>

void V(char *str, int len)
{
int i,j;
double temp,p;
FILE *fp;
FILE *f;

fp = fopen(str,"r");
f = fopen("vdis.dat","w");


while(fscanf(fp,"%lf",&p)!=EOF)
{
//Generate numbers
temp = (-2) * (log(1-p));
fprintf(f,"%lf\n",temp);
}
fclose(fp);
fclose(f);
}

int main()
{

    V("uni.dat",1000000);
    return 0;
}
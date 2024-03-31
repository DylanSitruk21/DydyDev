#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <ctime>

void showbits(short s);
void showValue (short s, int n);
float value (short s, int n);
double mult_q15 (short a, short b);
int* conv(int *a,int *b,int n,int m,int *y);

int main() {
    int x[4096];
    int h[4096];
    float t;

    clock_t start_t,end_t;

    for (int j = 0; j < 4096; ++j) {
        x[j]=rand();
        h[j]=rand();
    }

    int* y;
    y=(int*)malloc((4096+4096-1)*sizeof(int));
    start_t=clock();
    conv(x,h,4096,4096,y);
    end_t=clock();
    t=(float)(end_t-start_t)/CLOCKS_PER_SEC;
    printf("Total time taken by CPU: %f\n",t);
    /*if(y!=NULL){
        for (int i = 0; i < 8; i++) {
            printf("%2.2f ",y[i]);
        }
    }*/
    free (y);

    return 0;
}

double mult_q15 (short a, short b){
    float a_q15=value(a,15);
    float b_q15=value(b,15);
    return (double)a_q15*b_q15;
}

float value(short s, int n){
    return (float)s/pow(2,n);
}


void showValue (short s, int n){
    float number=(float)s/pow(2,n);
    printf("%f\n",number);
}


void showbits(short s){
    int bits[16];
    short temp=s;

    for (int i = 0; i < 16; i++) {
        bits[15-i]=temp&1;
        temp=temp>>1;
    }

    for (int i = 0; i < 16 ; i++) {
        if (i%4==0 && i>0)
            printf(" ");
        printf("%d",bits[i]);
    }
}

int* conv(int *a,int *b,int n,int m,int *y){
    int lengthFirstVector=0,lengthSecVector=0;
    int totalLengthVector=n+m-1;
    float temp=0;

    for (lengthFirstVector=0; lengthFirstVector<=totalLengthVector-1; lengthFirstVector++){
        for (lengthSecVector=0; lengthSecVector<=lengthFirstVector; lengthSecVector++){
            if(lengthFirstVector-lengthSecVector<m && lengthSecVector<n){
                temp += a[lengthSecVector]*b[lengthFirstVector-lengthSecVector];
            }
        }
        y[lengthFirstVector]=temp;
        temp=0;
    }

    return &y[0];
}

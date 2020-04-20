#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>
#include <math.h>


bool intersectLineCircle(double a, double b, double c, double x, double y, double r){
    double dist = fabs(a*x + b*y + c) / (sqrt(a*a + b*b));
    if(r > dist){
        return true;
    }
    return false;
}

int intersectLineCircle2(double left, double d){
    // Idea was taken from discussion with Farhan Ahmed
    // Basically get the left and right boundaries of the circle and you can get the number of intersects by using the floor
    // Floor is used since the vertical lines are on integer values
    double right = left - d;
    int intersects = floor(left) - floor(right);
    return intersects;
}

double getRandom(double min, double max){
    return min + ((double)rand() / ( (double)RAND_MAX / (double)(max-min) ) ) ;
}

void buffonDisc(int nlines, double d, int tosses){
    double randX;
    int intersects = 0;
    for(int i = 0; i < tosses; ++i){
        randX = getRandom(0.0, nlines);
        //printf("%f\n", randX);
        intersects += intersectLineCircle2(randX, d);
    }
    double prob = (double)  intersects / (double)tosses;
    printf("%d\n", intersects);
    printf("%d\n", tosses);
    printf("%f\n", prob);
}


int main(int argc, char const *argv[]){
    printf("Hello world\n");
    srand(time(0));
    clock_t start;
    clock_t end;
    int tosses = 1984000000;
    start = clock();
    buffonDisc(10, .75, tosses);
    end = clock();
    printf("\n Monte Carlo Time: %f\n", (double)(end - start)/CLOCKS_PER_SEC);
    return 0;
}
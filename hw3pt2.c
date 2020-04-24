#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>
#include <math.h>

double getRandom(double min, double max){
    return min + ((double)rand() / ( (double)RAND_MAX / (double)(max-min) ) ) ;
}

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

void buffonDisc(int nlines, double d, int tosses){
    double randX;
    int intersects = 0;
    int intersectsOnce = 0;
    int intersectsTwice = 0;
    int intersectsThrice = 0;
    int intersectsFour = 0;
    int intersectsFive = 0;
    int intersectsSix = 0;
    int intersectsSeven = 0;
    int intersectsEight = 0;
    int intersectsNine = 0;
    int intersectsTen = 0;
    for(int i = 0; i < tosses; ++i){
        randX = getRandom(0.0, nlines);
        //printf("%f\n", randX);
        intersects = intersectLineCircle2(randX, d);
        switch (intersects)
        {
        case 10:
            ++intersectsTen;
        case 9:
            ++intersectsNine;
        case 8:
            ++intersectsEight;
        case 7:
            ++intersectsSeven;
        case 6:
            ++intersectsSix;
        case 5:
            ++intersectsFive;
        case 4:
            ++intersectsFour;
        case 3:
            ++intersectsThrice;
        case 2:
            ++intersectsTwice;
        case 1:
            ++intersectsOnce;
        default:
            break;
        }
    }
    double probOnce = (double)  intersectsOnce / (double)tosses;
    double probTwice = (double)  intersectsTwice / (double)tosses;
    double probThrice = (double)  intersectsThrice / (double)tosses;
    double probFour = (double)  intersectsFour / (double)tosses;
    double probFive = (double)  intersectsFive / (double)tosses;
    double probSix = (double)  intersectsSix / (double)tosses;
    double probSeven = (double)  intersectsSeven / (double)tosses;
    double probEight = (double)  intersectsEight / (double)tosses;
    double probNine = (double)  intersectsNine / (double)tosses;
    double probTen = (double)  intersectsTen / (double)tosses;
    printf("Below is the probabilities of a disk of diameter %f\n", d);
    printf("The probability of a disk crossing once is %f\n", probOnce);
    if(d > 1){
        printf("The probability of a disk crossing twice is %f\n", probTwice);
        printf("The probability of a disk crossing thrice is %f\n", probThrice);
        printf("The probability of a disk crossing four times is %f\n", probFour);
        printf("The probability of a disk crossing five times is %f\n", probFive);
        printf("The probability of a disk crossing six times is %f\n", probSix);
        printf("The probability of a disk crossing seven times is %f\n", probSeven);
        printf("The probability of a disk crossing eight times is %f\n", probEight);
        printf("The probability of a disk crossing nine times is %f\n", probNine);
        printf("The probability of a disk crossing ten times is %f\n", probTen);
    }
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
    printf("Buffon's Disc Time: %f\n", (double)(end - start)/CLOCKS_PER_SEC);
    printf("Running EXTRA CREDIT\n");
    start = clock();
    buffonDisc(10, .1, tosses);
    buffonDisc(10, .2, tosses);
    buffonDisc(10, .3, tosses);
    buffonDisc(10, .4, tosses);
    buffonDisc(10, .5, tosses);
    buffonDisc(10, .6, tosses);
    buffonDisc(10, .7, tosses);
    buffonDisc(10, .8, tosses);
    buffonDisc(10, .9, tosses);
    buffonDisc(10, 1.5, tosses);
    buffonDisc(10, 2, tosses);
    buffonDisc(10, 3, tosses);
    end = clock();
    printf("EXTRA CREDIT Buffon's Disc Time: %f\n", (double)(end - start)/CLOCKS_PER_SEC);
    return 0;
}
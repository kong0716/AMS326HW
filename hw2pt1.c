#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
void generateRandomMatrix(int n, double **matrix);
void showMatrix(int n, double **matrix);
void matrixMultiply(int n, double **A, double **B, double **C);
void matrixSum(int n, double **A, double **B, double **C);
void strassen(int n, double **A, double **B, double **C, int n0);
void matrixSub(int n, double **A, double **B, double **result);

void free2darray(int n, double** A){
    double *currentIntPtr = NULL;
    for (int i = 0; i < n; i++)
    {
        currentIntPtr = A[i];
        free(currentIntPtr);    
    }
    free(A);
}

void reset2darray(int n, double** A){
    free2darray(n, A);
    A = (double **)malloc((n) * sizeof(double *));

    for (int i = 0; i < n; i++){
        A[i] = (double *)malloc((n) * sizeof(double *));
    }

}
//Generate a random matrix
void generateRandomMatrix(int n, double **matrix){   
    srand(time(NULL));
    for (size_t i = 0; i < n; i++){
        for (size_t j = 0; j < n; j++){
            matrix[i][j] = rand() % 20 + (-10);
            //matrix[i][j] = ((double)rand() / (double)RAND_MAX);
        }
    }
}
void showMatrix(int n, double **matrix){
    for (size_t i = 0; i < n; i++)
    {
        if (i == 0)
        {
            printf(" [ ");
        }
        else
        {
            printf("[ ");
        }
        for (size_t j = 0; j < n; j++)
        {
            printf(" %g ", matrix[i][j]);
        }
        printf(" ]\n ");
    }
}
void matrixMultiply(int n, double **A, double **B, double **result){
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
        {
            result[i][j] = 0;
            for (int k = 0; k < n; k++)
                result[i][j] += A[i][k] * B[k][j];
        }
}
void matrixSum(int n, double **A, double **B, double **result){
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            result[i][j] = A[i][j] + B[i][j];
}
void matrixSub(int n, double **A, double **B, double **result){
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            result[i][j] = A[i][j] - B[i][j];
}

int main(int argc, char const *argv[])
{
    int n = 1024;
    int n0 = 256;
    double **A, **B, **C;
    clock_t start;
    clock_t end;
    //Principal matrix
    A = (double **)malloc(n * sizeof(double *));
    B = (double **)malloc(n * sizeof(double *));
    C = (double **)malloc(n * sizeof(double *));
    for (int i = 0; i < n; i++)
    {
        A[i] = (double *)malloc(n * sizeof(double *));
        B[i] = (double *)malloc(n * sizeof(double *));
        C[i] = (double *)malloc(n * sizeof(double *));
    }
    generateRandomMatrix(n, A);
    generateRandomMatrix(n, B);
    printf("\tMatrix A of size %d x %d :\n", n, n);
    //showMatrix(n, A);
    printf("\tMatrix B of size %d x %d :\n", n, n);
    //showMatrix(n, B);
    start = clock();
    strassen(n, A, B, C, n0);
    end = clock();
    printf("\tC\n");
    //showMatrix(n, C);
    printf("\n Strassen time: %f\n", (double)(end - start)/CLOCKS_PER_SEC);

    start = clock();
    matrixMultiply(n, A, B, C);
    end = clock();
    printf("\tC\n");
    //showMatrix(n, C);
    printf("\n Naive time: %f\n", (double)(end - start)/CLOCKS_PER_SEC);
    for (int i = 0; i < n; i++)
    {
        double *currentIntPtr = A[i];
        free(currentIntPtr);
        currentIntPtr = B[i];
        free(currentIntPtr);
        currentIntPtr = C[i];
        free(currentIntPtr);
    }
    free(A);
    free(B);
    free(C);

    
    n = 4096;
    A = (double **)malloc(n * sizeof(double *));
    B = (double **)malloc(n * sizeof(double *));
    C = (double **)malloc(n * sizeof(double *));
    for (int i = 0; i < n; i++)
    {
        A[i] = (double *)malloc(n * sizeof(double *));
        B[i] = (double *)malloc(n * sizeof(double *));
        C[i] = (double *)malloc(n * sizeof(double *));
    }
    generateRandomMatrix(n, A);
    generateRandomMatrix(n, B);
    printf("\tMatrix A of size %d x %d :\n", n, n);
    //showMatrix(n, A);
    printf("\tMatrix B of size %d x %d :\n", n, n);
    //showMatrix(n, B);
    start = clock();
    strassen(n, A, B, C, n0);
    end = clock();
    printf("\tC\n");
    //showMatrix(n, C);
    printf("\n Strassen time: %f\n", (double)(end - start)/CLOCKS_PER_SEC);

    start = clock();
    matrixMultiply(n, A, B, C);
    end = clock();
    printf("\tC\n");
    //showMatrix(n, C);
    printf("\n Naive time: %f\n", (double)(end - start)/CLOCKS_PER_SEC);

    for (int i = 0; i < n; i++)
    {
        double *currentIntPtr = A[i];
        free(currentIntPtr);
        currentIntPtr = B[i];
        free(currentIntPtr);
        currentIntPtr = C[i];
        free(currentIntPtr);
    }
    free(A);
    free(B);
    free(C);
    
    return 0;
}

void strassen(int n, double **A, double **B, double **C, int n0)
{
    int i, j, k = 0;
    double **A11, **A12, **A21, **A22, **B11, **B12, **B21, **B22, **S1, **S2, **M1, **M2, **M3, **M4, **M5, **M6, **M7, **C11, **C12, **C21, **C22;

    A11 = (double **)malloc((n / 2) * sizeof(double *));
    A12 = (double **)malloc((n / 2) * sizeof(double *));
    A21 = (double **)malloc((n / 2) * sizeof(double *));
    A22 = (double **)malloc((n / 2) * sizeof(double *));
    B11 = (double **)malloc((n / 2) * sizeof(double *));
    B12 = (double **)malloc((n / 2) * sizeof(double *));
    B21 = (double **)malloc((n / 2) * sizeof(double *));
    B22 = (double **)malloc((n / 2) * sizeof(double *));
    S1 = (double **)malloc((n / 2) * sizeof(double *));
    S2 = (double **)malloc((n / 2) * sizeof(double *));
    M1 = (double **)malloc((n / 2) * sizeof(double *));
    M2 = (double **)malloc((n / 2) * sizeof(double *));
    M3 = (double **)malloc((n / 2) * sizeof(double *));
    M4 = (double **)malloc((n / 2) * sizeof(double *));
    M5 = (double **)malloc((n / 2) * sizeof(double *));
    M6 = (double **)malloc((n / 2) * sizeof(double *));
    M7 = (double **)malloc((n / 2) * sizeof(double *));
    C11 = (double **)malloc((n / 2) * sizeof(double *));
    C12 = (double **)malloc((n / 2) * sizeof(double *));
    C21 = (double **)malloc((n / 2) * sizeof(double *));
    C22 = (double **)malloc((n / 2) * sizeof(double *));

    for (int i = 0; i < n / 2; i++)
    {
        A11[i] = (double *)malloc((n / 2) * sizeof(double *));
        A12[i] = (double *)malloc((n / 2) * sizeof(double *));
        A21[i] = (double *)malloc((n / 2) * sizeof(double *));
        A22[i] = (double *)malloc((n / 2) * sizeof(double *));
        B11[i] = (double *)malloc((n / 2) * sizeof(double *));
        B12[i] = (double *)malloc((n / 2) * sizeof(double *));
        B21[i] = (double *)malloc((n / 2) * sizeof(double *));
        B22[i] = (double *)malloc((n / 2) * sizeof(double *));
        S1[i] = (double *)malloc((n / 2) * sizeof(double *));
        S2[i] = (double *)malloc((n / 2) * sizeof(double *));
        M1[i] = (double *)malloc((n / 2) * sizeof(double *));
        M2[i] = (double *)malloc((n / 2) * sizeof(double *));
        M3[i] = (double *)malloc((n / 2) * sizeof(double *));
        M4[i] = (double *)malloc((n / 2) * sizeof(double *));
        M5[i] = (double *)malloc((n / 2) * sizeof(double *));
        M6[i] = (double *)malloc((n / 2) * sizeof(double *));
        M7[i] = (double *)malloc((n / 2) * sizeof(double *));
        C11[i] = (double *)malloc((n / 2) * sizeof(double *));
        C12[i] = (double *)malloc((n / 2) * sizeof(double *));
        C21[i] = (double *)malloc((n / 2) * sizeof(double *));
        C22[i] = (double *)malloc((n / 2) * sizeof(double *));
    }
    if (n < n0) //2-order
    {
        matrixMultiply(n, A, B, C);
    }
    else
    {   //Split the matrix
        for (i = 0; i < n / 2; i++)
        {
            for (j = 0; j < n / 2; j++)
            {
                A11[i][j] = A[i][j];
                A12[i][j] = A[i][j + n / 2];
                A21[i][j] = A[i + n / 2][j];
                A22[i][j] = A[i + n / 2][j + n / 2];

                B11[i][j] = B[i][j];
                B12[i][j] = B[i][j + n / 2];
                B21[i][j] = B[i + n / 2][j];
                B22[i][j] = B[i + n / 2][j + n / 2];
            }
        }
        matrixSum(n/2, A11, A22, S1);
        matrixSum(n/2, B11, B22, S2);
        strassen(n/2, S1, S2, M1, n0);


        matrixSum(n/2, A21, A22, S1);
        strassen(n/2, S1, B11, M2,n0);

        matrixSub(n/2, B12, B22, S1);
        strassen(n/2, A11, S1, M3, n0);

        matrixSub(n/2, B21, B11, S1);
        strassen(n/2, A22, S1, M4, n0);

        matrixSum(n/2, A11, A12, S1);
        strassen(n/2, S1, B22, M5, n0);

        matrixSub(n/2, A21, A11, S1);
        matrixSum(n/2, B11, B12, S2);
        strassen(n/2, S1, S2, M6, n0);

        matrixSub(n/2, A12, A22, S1);
        matrixSum(n/2, B21, B22, S2);
        strassen(n/2, S1, S2, M7, n0);

        matrixSum(n/2, M1, M4, S1);
        matrixSub(n/2, S1, M5, S2);
        matrixSum(n/2, S2, M7, C11);


        matrixSum(n/2, M3, M5, C12);

        matrixSum(n/2, M2, M4, C21);

        matrixSub(n/2, M1, M2, S1);
        matrixSum(n/2, S1, M3, S2);
        matrixSum(n/2, S2, M6, C22);

        for (i = 0; i < n / 2; i++)
        {
            for (j = 0; j < n / 2; j++)
            {
                C[i][j] = C11[i][j];
                C[i][j + n / 2] = C12[i][j];
                C[i + n / 2][j] = C21[i][j];
                C[i + n / 2][j + n / 2] = C22[i][j];
            }
        }
    }

    double *currentIntPtr = NULL;
    for (int i = 0; i < n/2; i++)
    {
        currentIntPtr = A11[i];
        free(currentIntPtr);
        currentIntPtr = A12[i];
        free(currentIntPtr);
        currentIntPtr = A21[i];
        free(currentIntPtr);
        currentIntPtr = A22[i];
        free(currentIntPtr);
        currentIntPtr = B11[i];
        free(currentIntPtr);
        currentIntPtr = B12[i];
        free(currentIntPtr);
        currentIntPtr = B21[i];
        free(currentIntPtr);
        currentIntPtr = B22[i];
        free(currentIntPtr);
        currentIntPtr = C11[i];
        free(currentIntPtr);
        currentIntPtr = C12[i];
        free(currentIntPtr);
        currentIntPtr = C21[i];
        free(currentIntPtr);
        currentIntPtr = C22[i];
        free(currentIntPtr);
        currentIntPtr = M1[i];
        free(currentIntPtr);
        currentIntPtr = M2[i];
        free(currentIntPtr);
        currentIntPtr = M3[i];
        free(currentIntPtr);
        currentIntPtr = M4[i];
        free(currentIntPtr);
        currentIntPtr = M5[i];
        free(currentIntPtr);
        currentIntPtr = M6[i];
        free(currentIntPtr);
        currentIntPtr = M7[i];
        free(currentIntPtr);
        currentIntPtr = S1[i];
        free(currentIntPtr);
        currentIntPtr = S2[i];
        free(currentIntPtr);             
    }
    free(A11);
    free(A12);
    free(A21);
    free(A22);
    free(B11);
    free(B12);
    free(B21);
    free(B22);
    free(C11);
    free(C12);
    free(C21);
    free(C22);
    free(M1);
    free(M2);
    free(M3);
    free(M4);
    free(M5);
    free(M6);
    free(M7);
    free(S1);
    free(S2);
    
}
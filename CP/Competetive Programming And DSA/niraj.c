int main()
{
    int A;
    printf("Enter the number A: ");
    scanf("%d", &A);
    int i;
    printf("Select the option:\n 1. Check Whether number is positive or negative \n2.Get the table of given number");
    scanf("%d", &i);
    switch(i) {
        case 1:
                if(A>=0){
                    printf("The Number is Positive");
                }else{
                    printf("The number is negative");

                }
        case 2:
                int m = 1;
                while(m=10){
                    printf("%d",A*m);
                    m++;
                }
    }
    return 0;

}
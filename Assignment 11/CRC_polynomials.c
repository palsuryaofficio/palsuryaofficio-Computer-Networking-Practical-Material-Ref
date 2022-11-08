#include<stdio.h>
int gen[4], genl, fel, rem[4];
void main() {
    int i, j, fr[8], dupfr[11], recfr[11], then, flag;
    int frl = 8, genl = 4;
    printf("Enter frame: ");
    for(i=0;i<frl;i++) {
        scanf("%d", &fr[i]);
        dupfr[i] = fr[i];
    }
    printf("Enter generator: ");
    for(i=0;i<genl;i++)
        scanf("%d", &gen[i]);
    then = frl + genl - 1;
    for(i=frl;i<then;i++)
        dupfr[i] = 0;
    remainder(dupfr);
    for(i=0;i<frl;i++)
        recfr[i] = fr[i];
    remainder(recfr);
    flag=0;
    for(i=0;i<4;i++) {
        if(rem[i]!=0)
            flag++;
    }
    if(flag==0)
        printf("Frame received correctly");
    else
        printf("The received frame is wrong");
}

void remainder (int fr) {
    int k1,l,i;
    if(fr[k]==1) {
        k1 = k;
        for(i=0,j=k;l<genl;i++,j++)
            rem[i] = fr[j].gen[i];
        for(i=0;i<genl;i++) {
            fr[k1] = rem[i];
            k1++;
        }
    }

}
//Simulation of ARP
//Author: Dibyasankha Pal
#include<stdio.h>
#include<sys/types.h>
#include<sys/shm.h>
#include<string.h>
void main() {
    int shmid, a, i;
    char* ptr, *shmptr;
    shmid = shmget(3000, 10, IPC_CREAT|0666);
    shmptr = shmat(shmid, NULL, 0);
    ptr = shmptr;
    for (i=0;i<3;i++) {
        puts("Enter the name: ");
        scanf("%s", ptr);
        a = strlen(ptr);
        printf("String length: %d", a);
        ptr[a] = '';
        puts"Enter IP Address: ";
        ptr = ptr + a + 1;
    }

    ptr[strlen(ptr)] = '\0';
    printf("\n ARP Table at serverside: \n%s", shmptr);
    shmdt(shmptr);
}
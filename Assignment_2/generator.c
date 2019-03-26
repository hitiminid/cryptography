#include<stdlib.h>
#include<stdio.h>

int main(int argc, char **argv) {
	int seed;

	if (argc < 2) {
		printf("Not enough data");
		return 0;
	}
	
	if (argc == 3) {
    	seed = atoi(argv[2]);        
    }

    srandom(seed);		
    int numberOfElements = atoi(argv[1]);
    for (int i = 0; i < numberOfElements; i++) {
        printf("%ld\n", random());
    }
    return 0;
}

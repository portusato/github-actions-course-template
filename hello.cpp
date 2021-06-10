#include <iostream>
#include <cstdio>
#include <string.h>

#include "stdio.h"
using namespace std;

void print_and_increment(int i);
bool IsPasswordOK(void);

int main() {
    IsPasswordOK();
    std::cout << "Hello World!\n";
    print_and_increment(5);
    
    return 0;
}

void print_and_increment(int i) {
    std::cout << i++ << i << std::endl;
}

bool IsPasswordOK(void) {
    char buffer[12];
    char offset[6];
    std::cout << "Enter offset: ";
    fgets(offset, 6, stdin);
    std::cout << buffer [int(offset)];
}

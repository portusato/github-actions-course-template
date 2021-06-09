#include <iostream>

void print_and_increment(int i);

int main() {
    std::cout << "Hello World!\n";
    print_and_increment(5);
    return 0;
}

void print_and_increment(int i) {
    std::cout << i++ << i << std::endl;
}

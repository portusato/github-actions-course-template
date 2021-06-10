#include <iostream>

void print_and_increment(int i);

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
    char password[12];
    gets(password);
    return 0 == strcmp(password, "goodpass");
}

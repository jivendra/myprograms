#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    int a = 5;
    int* p;           //pointer variable
    p = &a;           //& gives the address of a variable and we are allocating the address to a pointer variable
    cout << a << endl; //prints value of a
    cout << p << endl; //prints address of a, because value of p is address of a
    cout << &a << endl; //Prints address of a
    cout<< &p << endl; //prints address of p
    cout<< *p << endl; //prints the value at the address which p stores, it will print the value os a
    // This concept is called as dereferencing
    *p = 1024; //now the value of a canged, we changes its value by accessing it with its address
    cout << a <<endl;
    char *q;
    q = (char*)p; //pointer tyecasting, now q will store the value of p, which is address of a
    cout << *q << endl;

    int *n = NULL; //This is NULL pointer which points to nothing
    cout << endl;
    return 0;
}
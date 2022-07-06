#include <iostream>
using namespace std;

int main() {
    //Pointer and array
    //Name of array is also a pointer to the first element of array
    //vice versa is also true - pointer to first element of array acts as name of array
    char c[] = {'a', 'b', 'c'};
    char *p = c; //p points to c[0]
    char *q = &c[0]; //q points to c[0]
    cout << c[0] << p[0] << q[0];
    cout << endl;
    return 0;
}
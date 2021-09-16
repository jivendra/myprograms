//stringstream program https://www.hackerrank.com/challenges/c-tutorial-stringstream/problem
#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
    stringstream s(str);
    vector<int> vect;    
    int i=0;
	int a;
    char ch;
    while(s>>a){
        vect.push_back(a);
        s>>ch;
        i++;
    }    
    return vect;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}
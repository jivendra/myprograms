#include<bits/stdc++.h>
using namespace std;

int binary_search(int* arr, int size, int query){
    int l = 0, r = size-1;
    if(query < arr[l] || query > arr[r])
    return -1;
    int mid,guess;
    while(l <= r){
        mid = (l+r)/2;
        guess = arr[mid];
        if(guess == query)
            return mid+1;
        if(guess > query)
            r = mid;
        else
            l = mid;
    }
    return 0;
}
int main(){
    int size;
    cin>>size;
    int arr[size];
    for (size_t i = 0; i < size; i++)
    cin>>arr[i];

    int query;
    cin>>query;
    int result = binary_search(arr,size,query);
    if(result == -1)
    cout<<"Element not present";
    else
    cout<<"Position : "<<result;
    return 0;
}
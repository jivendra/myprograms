#include<iostream>
using namespace std;

int main() {
	int arr[] = { 10,14,2,17,34,21 };
	int min_index;
	for (int i = 0; i < 5; i++) {
		min_index = i;
		for (int j = i + 1; j < 6; j++) {
			if (arr[j] < arr[min_index])
				min_index = j;
		}
		swap(arr[min_index], arr[i]);
	}
	for (int i = 0; i < 6; i++)
		cout << arr[i] << " ";
	cout << endl;
}
#include <iostream>
#include "BubbleSort.cpp"
#include "MergeSort.cpp"

using std::cout, std::endl;

int main() {
  const int size = 2;
  int arr[size] = {64, 65};

  // cout << "unsorted: ";
  // for (int i = 0; i < size; i++) {
  //   cout << arr[i] << ", ";
  // }
  // cout << endl;
  SortLib::BucketSort(arr, size);
  // cout << "sorted: ";
  // for (int i = 0; i < size; i++) {
  //   cout << arr[i] << ", ";
  // }
  // cout << endl;


  return 0;
}

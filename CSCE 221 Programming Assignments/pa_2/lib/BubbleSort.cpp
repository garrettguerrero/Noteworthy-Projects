#include "SortLib.h"

template <typename T>
void SortLib::BubbleSort(T arr[], int size) {

  // swap each pair of elements where the second is smaller than the first (elements 0 and 1, 1 and 2, 2 and 3)
  // loop until no swaps are performed after a full iteration of the array
  bool swap = true;
  T temp;
  while (swap) {
    swap = false;
    for (int i = 0; i < size - 1; i++) {
      if (arr[i] > arr[i + 1]) {
        temp = arr[i];
        arr[i] = arr[i + 1];
        arr[i + 1] = temp;
        swap = true;
      }
    }
  }

}

template void SortLib::BubbleSort(int*, int);

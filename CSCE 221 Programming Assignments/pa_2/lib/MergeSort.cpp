#include "SortLib.h"

template <typename T>
void SortLib::MergeSort(T arr[], int size) {
  if (size == 1) {
    return;
  }

  // create two new arrays in which to put each half of arr elements
  int size_1;
  int size_2;
  if (size % 2 != 0) {
    size_1 = (size / 2);
    size_2 = (size / 2) + 1;
  } else {
    size_1 = size / 2;
    size_2 = size / 2;
  }
  T* arr_1 = new T[size_1];
  T* arr_2 = new T[size_2];

  int i;
  for (i = 0; i < size_1; i++) {
    arr_1[i] = arr[i];
  }

  for (i = 0; i < size_2; i++) {
    arr_2[i] = arr[size_1 + i];
  }
  // if size is not 1, call merge sort for each half
  MergeSort(arr_1, size_1);
  MergeSort(arr_2, size_2);

  // combine the two arrays, sorting them as they are placed into arr
  int index_1 = 0;
  int index_2 = 0;
  i = 0;
  while (index_1 < size_1 && index_2 < size_2) {
    if (arr_1[index_1] < arr_2[index_2])
      arr[i++] = arr_1[index_1++];
    else
      arr[i++] = arr_2[index_2++];
  }

  while (index_1 < size_1)
    arr[i++] = arr_1[index_1++];

  while (index_2 < size_2)
    arr[i++] = arr_2[index_2++];

  delete[] arr_1;
  delete[] arr_2;
}

template void SortLib::MergeSort(int*, int);

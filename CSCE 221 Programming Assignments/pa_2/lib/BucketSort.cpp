#include "SortLib.h"


template <typename T>
void SortLib::BucketSort(T arr[], int size) {
  if (size == 1) return;
  // find max and min
  int i;
  int max = arr[0];
  int min = arr[0];

  for (i = 0; i < size; i++) {
    if (max < arr[i])
      max = arr[i];
    if (min > arr[i])
      min = arr[i];
  }

  // make a new array with the side of max - min
  int bucket_size = max - min + 1;
  T* buckets = new T[bucket_size];
  for (i = 0; i < bucket_size; i++)
    buckets[i] = 0;

  // iterate through arr and add to count of each corresponding spot in bucket list
  for (i = 0; i < size; i++) {
    buckets[arr[i] - min]++;
  }

  // move values back into arr from bucket
  int k = 0;
  for (i = 0; i < bucket_size; i++) {
    if (buckets[i] > 0) {
      int j = buckets[i];
      while (j > 0) {
        arr[k++] = i + min;
        j--;
      }
    }
  }

  delete[] buckets;
}

template void SortLib::BucketSort(int*, int);

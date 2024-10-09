#include <iostream>

// Mark Crawford
// Professor Lucci, Algorithms, CCNY
// quick_sort.cpp
// Algorithm for quick sort
// Quick sort is unstable (will not preserve positions of equal value elements)
// If choosing a pivot element at the end, as here, the worst case complexity is O(n^2)
// This is because finding the pivot index may result in a pivot with all elements on one side (already sorted list)
// Methods of finding partition: naive, Lomuto, Hoare
//
// Lomuto is used here.

int partition(int arr[], int low, int high);
void quick_sort_rec(int arr[], int low, int high);
void quick_sort(int arr[], int len);
void print_array(int arr[], int len);
void swap(int *a, int *b);

int main() {
  int arr[10] = {100, 70, 30, 10, 40, 20, 80, 90, 50, 60};
  int length = 10;
  
  print_array(arr, length);
  quick_sort(arr, length);
  print_array(arr, length);

  return 0;
}


int partition(int arr[], int low, int high) {
  // Choosing last element as pivot
  int pivot = arr[high];
  int i = low - 1;
  for(int j = low; j <= high; j++) {
    if (arr[j] < pivot) {
      i++;
      swap(&arr[i], &arr[j]);
    }
  }

  swap(&arr[i+1], &arr[high]);
  return i + 1;
}

void quick_sort_rec(int arr[], int low, int high) {
  // if (low < high) to establish base case
  if (low < high) {
    
    // Find partition index
    int partition_index = partition(arr, low, high);
    // Recursive calls on left and right
    quick_sort_rec(arr, low, partition_index - 1);
    quick_sort_rec(arr, partition_index + 1, high);

  }
}

void quick_sort(int arr[], int len) {
  quick_sort_rec(arr, 0, len - 1);
}

void print_array(int arr[], int len) {
  for(int i = 0; i < len; i++) {
    std::cout << arr[i] << " ";
  }
  std::cout << "\n\n";
}

void swap(int *a, int *b) {
  int c = *a;
  *a = *b;
  *b = c;
}


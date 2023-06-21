Each of these sorting algorithms has its strengths and weaknesses, and understanding their differences can help us choose the most appropriate algorithm for a given task. By implementing and comparing these sorting algorithms, we can gain a deeper understanding of how they work and how to choose the best algorithm for a given problem.
this project compleatoin will be a "Sorting algorithm vissualizer" 
fisrt commit is this 5 algorithm , to be continued.
**Selection Sort:**
Selection Sort is a simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the array and placing it at the beginning of the array. This process is repeated until the entire array is sorted. Selection Sort is easy to understand and implement, but it has a time complexity of O(n^2), which makes it inefficient for large arrays. Despite its inefficiency, Selection Sort can be useful for small arrays or as a building block for more complex sorting algorithms.

**Bubble Sort:**
Bubble Sort is another simple sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order until the array is sorted. In each iteration, the largest element is bubbled up to the end of the array. Bubble Sort has a time complexity of O(n^2) and is generally less efficient than other sorting algorithms. However, it is easy to understand and implement, making it a good choice for small arrays or as a teaching tool for introductory programming courses.

**Insertion Sort:**
Insertion Sort is a sorting algorithm that works by iterating through the array and inserting each element into its proper position in the sorted part of the array. The sorted part of the array starts with the first element and grows as each subsequent element is inserted. Insertion Sort has a time complexity of O(n^2) for worst-case scenarios, but it can be faster than other sorting algorithms for small arrays or partially sorted arrays. Insertion Sort is also useful for sorting linked lists since it requires only constant extra space.

**Merge Sort:**
Merge Sort is a more advanced sorting algorithm that works by dividing the array into two halves, sorting each half, and then merging the sorted halves back together. Merge Sort has a time complexity of O(n log n) and is considered one of the most efficient comparison-based sorting algorithms. Merge Sort is also a stable sorting algorithm, meaning that it does not change the relative order of equal elements in the input array.

**Quick Sort:**
Quick Sort is another advanced sorting algorithm that works by selecting a pivot element and partitioning the array around the pivot, recursively sorting each partition. Quick Sort has a time complexity of O(n log n) in the average and best cases, but it can have a worst-case scenario of O(n^2) if the pivot is not chosen correctly. Quick Sort is a popular sorting algorithm due to its efficiency and can be faster than Merge Sort in certain scenarios. Quick Sort is also an in-place sorting algorithm, meaning that it does not require extra memory for sorting.

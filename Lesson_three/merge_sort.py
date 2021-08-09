"""
In computer science, merge sort is an efficient, general-purpose, and comparison-based sorting algorithm.
Most implementations produce a stable sort, which means that the order of equal elements is the same in the input and output


Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, 
and then merges the two sorted halves. 

The merge() function is used for merging two halves.  The merge(arr, l, m, r) is a key process that assumes that arr[l..m] 
and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.

Sorting is pretty tedious—take a break and check out this comic inspired by merge sort. https://xkcd.com/1185/
You can learn more about merge sort, as well as see many more visualizations, in the online Algorithms textbook https://algs4.cs.princeton.edu/22mergesort/
https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Merge_sort_algorithm_diagram.svg/300px-Merge_sort_algorithm_diagram.svg.png
"""

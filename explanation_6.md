
### Implementation

- As for union, only one set is needed to keep the unique value between two linked list
- As for intersection, two sets are needed to keep the unique value between two linked list, and use the built-in function of set--intersection to get the result.

define number of nodes:n
Worst case time:  
1. union func includes three loops: O(2n)+O(2n)+O(n)=O(5n)-> O(n)
2. intersection func includes three loops: O(2n)+O(2n)+O(n)=O(5n)-> O(n)
So the final Worst case time is O(n)

Space complexity: O(n)

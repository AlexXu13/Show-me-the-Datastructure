
### Implementation

- As for completing recursion easily, In here, I add a list "findfiles" as a new function parameter.
- if not given correct path name, it would assert an error.
- By using os.listdir to read all of name of the files in given path, if it is a file, and ends with the suffix name, the absolute path of corresponding file will be added into findfiles list; if 
it is a dir name, recall the find_files fuction in this sub dir.

define dir number: n && average files number: f
Worst case time: T(n) = T(n - 1) + O(f);
T(n) = T(n - 1) + O(f)
= T(n - 2) + O(f) + O(f)
= T(n - 3) + O(f) + O(f) + O(f)
= ……
= O(f) + … + O(f) + O(f) + O(f)
= n * O(f)
= O(n*f)

Space complexity: O(n)

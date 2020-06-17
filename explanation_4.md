
### Implementation

If is_user_in_group return true,there are 3 cases:
- It's in parent group
- It's in child group, by using "key in list" to identify
- It's in subchild group, by using recursion

define group depth: n && average subgroup number: d
Worst case time: T(n) = O(n*d)
Space complexity: O(n*d)

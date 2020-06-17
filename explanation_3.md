
### Implementation

- I utilized two dicts in here, huffman dict is used to keep the occurences of each characters in a string
- And I utilized huffmantree dict to build huffman tree
- The charater with highest occurence is encoded with minimum code length

Worst case time:  
1. huffman_encoding func includes three for loops: O(n)+O(n)+O(n)=O(3n)-> O(n)
2. huffman_decoding func includes two for loops: O(n)+O(n) =O(2n)-> O(n)
So the final Worst case time is O(n)

Space complexity: O(n)

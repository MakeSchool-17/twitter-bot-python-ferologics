

**ARRAYS**

accesssing the array by memory pointer -  

A[4] = A[0] + s * i where s is the value and i the index


        *Dynamic array runtime*
______________________________________
                  |
    *Operation*   |    *Worst Case*
______________________________________
                  |
Access via index  |     o(1)
                  |  
 Insert element   |     O(n)
                  |
                  .
                  .
                  .
______________________________________

        *Linked list runtime*
______________________________________
                  |
                  |
                  |
                  |


*Hash function* - converts a variable-size input to a fixed-size output
same input -> same output

*Ideal Hash* (different for cryptographic hash functions) --->
    1. repeatable
    2. fast
    3. output is unsigned integer
    4. randomly distributes keys among output space
    5. small differences in input should result in large differences  in output

Hash buckets
    *bucket = hack(key) % n*
    - save the key and the value in the bucket (tuples)

*to resolve collisions*
    Linear probing -->
        * each bucket contains one object
        * on collision - go to next open bucket, add object there
        * to retrieve - find bucket, if that's not objet, iterate buckets until you find it

    Chaining -->
        * Each bucket contains a linked list

double hash probing?

Load factor - how full is your data structure

resize the hash table - once the load factor reaches a certain factor (usually 2/3)

+----------------------------------------------+
|       *Hash table complexity analysis*       |
+-------------+----------------+---------------+
|  Operation  |  Average case  |    Worst case |
+-------------+----------------+---------------+
|    Space    |      O(n)      |      O(n)     |
+-------------+----------------+---------------+
|    Search   |      O(1)      |      O(n)     |
+-------------+----------------+---------------+
|    Insert   |      O(1)      |      O(n)     |
+-------------+----------------+---------------+
|    Delete   |      O(1)      |      O(n)     |
+----------------------------------------------+

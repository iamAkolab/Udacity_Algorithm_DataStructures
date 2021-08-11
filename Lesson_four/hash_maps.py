"""
Hash Map in Python

Hash maps are indexed data structures. A hash map makes use of a hash function to compute an 
index with a key into an array of buckets or slots. Its value is mapped to the bucket with the 
corresponding index. The key is unique and immutable. Think of a hash map as a cabinet having 
drawers with labels for the things stored in them. For example, storing user information- consider 
email as the key, and we can map values corresponding to that user such as the first name, last name etc to a bucket. 

https://www.geeksforgeeks.org/hash-map-in-python/

String is as a key of the HashMap

When you create a HashMap object and try to store a key-value pair in it, while storing, 
a hash code of the given key is calculated and its value is placed at the position 
represented by the resultant hash code of the key.

When you pass the key to retrieve its value, the hash code is calculated again, and the 
value in the position represented by the hash code is fetched (if both hash codes are equal).

Suppose we used a certain variable as key to store data and later we modified the value of this 
variable. At the time of retrieval, since we changed the key, the hash code of the current key 
will not match with the hashCode at which its value has been stored making the retrieval impossible.

Since the String class is immutable, you cannot modify the value of a String once it is created. 
Therefore, it is recommended to use a String variable to hold keys in hash a map.

https://www.tutorialspoint.com/why-string-class-is-popular-key-in-a-hashmap-in-java
"""

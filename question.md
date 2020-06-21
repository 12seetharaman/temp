1.  What is the difference between a list and a tuple?

2. Difference types of methods in python
 - instance
 - static
 - class

3. Difference between the range and xrange in Python.
Answer: In terms of functionality, both range and xrange are identical. 
Both allow for generating a list of integers. 
The main difference between the two is that while range returns a Python list object, 
xrange returns an xrange object.

Xrange is not able to generate a static list at runtime the way range does. 
On the contrary, it creates values along with the requirements via a special technique called yielding. 
It is used with a type of object known as generators.

If you have a very enormous range for which you need to generate a list, then xrange is the function to opt for.
This is especially relevant for scenarios dealing with a memory-sensitive system, such as a smartphone.

The range is a memory beast. Using it requires much more memory, especially if the requirement is gigantic. 
Hence, in creating an array of integers to suit the needs, it can result in a Memory Error and ultimately lead to 
crashing the program.

4. Explain memory managed in Python? 
- Private heap

5. What does “self” refer to in a class?

6. Define a class named car with 2 attributes, “color” and “speed”. Then create an instance and return speed.
class Car :
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
car = Car('red','100mph')
car.speed
#=> '100mph'

7.  Explain how the map function works.

8. Are dictionaries or lists faster for lookups?
Looking up a value in a list takes O(n) time because the whole list needs to be iterated through until the value is found.
Looking up a key in a dictionary takes O(1) time because it’s a hash table.
This can make a huge time difference if there are a lot of values so dictionaries are generally recommended for speed. But they do have other limitations like needing unique keys.


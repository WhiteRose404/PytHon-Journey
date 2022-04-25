# PytHon-Journey
Python Journey is a simple, straight-forward programming course 👨‍💻 that will help you become comfortable programming in Python 3 🐍 and Beyond 🚀. This course built while i was studying for the python exam, since we didnt have a structure document for the course 💩, so this course was intended for me and my collegs at ENSIAS to help them pass with great success 🎉,


## Table Of Contents
1. [ Installation ](#installation)
2. [ Basic Operation. ](#basic-operation)
3. [ Lists. ](#lists)
4. [ Tuples. ](#tuples)
5. [ Sets. ](#sets)
6. [ Dictionary. ](#dictionary)
7. [ Arrays. ](#Arrays)
8. [ Search Algorithms ](#Search-Algorithms)
9. [ Sorting Algorithms. ](#Sorting-Algorithms)
10. [ Files. ](#Files)
11. [ Sqlite3 ](#Sqlite3)
12. [ Trees (Arber) ](#Trees)
13. [ Graph theory ](#Graph-theory)
14. [ Numpy ](#Numpy)
15. [ Numerical integration ](#integration)
16. [ Numerical methods for differential equations ](#differential-equations)
17. [ System of linear equations ](#linear-equations)


![download](https://user-images.githubusercontent.com/88856526/164738666-65244378-65f0-4ed3-b53d-1ee72e2fe714.jpeg)

# Installation

### Ubuntu
Python comes preinstalled on ubuntu in all recent releases.

![Kazam_screenshot_00007](https://user-images.githubusercontent.com/88856526/164764946-0a78a2f7-c747-404d-9733-f7946a9b3c69.png)

You can just type python in the terminal to access python 2 or python3 to Install python3. you would simply run: 
```
sudo apt update && sudo apt dist-upgrade
sudo apt install python3
```
To make sure that you've installed python successfully run:
```
python3 --version
```
you should see something like python version 3.10 or above.

### Mac




### Windows

# Basic Operation

Python divides the operators in the following groups:
<ul>
  <li><h3>Arithmetic operators</h3></li>
  <p>Arithmetic operators are used with numeric values to perform common mathematical operations:</p>
  <p>Addition + , Subtraction -, Multiplication *, Division /, Modulus %, Exponentiation **, Floor division	//.</p>
  <li><h3>Assignment operators</h3></li>
  <p>Assignment operators are used to assign values to variables:</p>
  <ul>
    <li><p>Using usual operation =, +=, -=, *=, , **=, %=, /=, //=</p></li>
    <li><p>Using binary opeation >>=, <<=, &=, |=, ^=</p></li>
  </ul>
  <p> In general A(ope)=B ===> A = A (ope) B </p>
  <p> For Example A+=B ===> A = A + B
  <li><h3>Comparison operators</h3></li>
  <p>Comparison operators are used to compare two values:</p>
  <p> == , <, >, <=, >=, !=.</p>
  <li><h3>Logical operators</h3></li>
  <p>Logical operators are used to combine conditional statements:</p>
  <ul>
    <li><p><strong>and:</strong>returns true if the two entries are true otherwise false</p></li>
    <li><p><strong>or:</strong>returns true if one of two entries is true otherwise false</p></li>
    <li><p><strong>not:</strong>reverse the result, returns False if the result is true</p></li>
  </ul>
    <p>For example :</p>
  <ul>
    <li><code>4>5 and 2<5 is False</code></li>
    <li><code>4>5 or 2<5 is True</code></li>
    <li><code>not  (4>5 and 2<5) is True</code></li>
  </ul>
  <li><h3>Identity operators</h3></li>
  <p>Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:</p>
  <ul>
    <li>is : Returns True if both variables are the same object</li>
    <li>is not: Returns True if both variables are not the same object</li>
  </ul>
  <code>
    A = "this is an object"; 
    B = A;
    A is B # Returns true since B is a refernce to A so A, B repersent the same object
  </code>
  <li><h3>Membership operators</h3></li>
    <p>Membership operators are used to test if a sequence is presented in an object:</p>
    <ul>
      <li>in: 	Returns True if a sequence with the specified value is present in the object</li>
      <li>not in: 	Returns True if a sequence with the specified value is not present in the object</li>
    </ul>   
    <li><h3>Bitwise operators</h3></li>
    <ul>
        <li>& Sets each bit to 1 if both bits are 1, for example 1 & 1 => 1 </li>
        <li>| Sets each bit to 1 if one of two bits is 1, for example 1 | 0 => 0</li>
        <li>^	Sets each bit to 1 if only one of two bits is 1, for example 1 & 1 => 0, 0 & 1 => 1,0 & 0 => 0</li>
        <li>~ Inverts all the bits for example ~1 => -2 (due to using 2's complement form).</li>
        <li><<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off for example 2<<3 = 16</li>
        <li>>> Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off for example 16>>3 = 2</li>
      </ul>
    </ul>
 </ul>
 
 # Lists

Lists are used to store multiple items in a single variable.<br>
Define a list:
```
lis1= ["Nice","appele",5]
lis2 = list(("Nice","appele",5))
lis3 = [ i for i in range(N)] # List Comprehensions
print(lis1,lis2,lis3)
```
#### Note
<p>List Comprehensions: A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.
for More info about the topic go to <a href=https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions>Docs</a></p>

### Mutable
Lists are mutable (changeable unlike sets or strings), meaning that we can change, add, and remove items in a list after it has been created.

```
lis1= ["Nice","appele",5]
print(lis1)
lis[1]="Banana"
print(lis1)
```
### Order
Lists are ordered, it means that the items have a defined order, and that order will not change.
```
lis1= ["Nice","appele",5]
print(lis1) # Notice the list is writing as the same order it was defined
```
### Duplicate
Allow Duplicates since lists are indexed, lists can have items with the same value.
```
lis1= ["Nice","Nice",4]
print(lis1)
```
### Flexible
Flexible allow multiple data type in a single list, and does not have a predefined length.
```
lis1= ["Nice","Appele",5] #  we already seen the flexiblity of python from the first example
lis1.append("eight") # <list datatype>.append(obj) a method used to add obj to the end of the list
print(lis1)
```
Finally from Python's perspective, lists are defined as objects with the data type 'list':
```
lis1= ["Nice","Appele",5]
print(type(lis1))
```
## Access Items
List items are indexed and you can access them by referring to the index number:
```
lis1= ["Nice","Appele",5]
print(lis1[2])
```
Negative Indexing: Negative indexing means start from the end
```
lis1= ["Nice","Appele",5]
print(lis1[-1])
```
You can specify a range of indexes by specifying where to start and where to end the range.
```
lis1= ["Nice","Appele",5,"54",8,"Me"]
print(lis1[0:4]) # the same as lis1[:4]
print(lis1[1:len(lis1)-1]) # the same as lis1[1:]
```
### Note
When specifying a range, the return value will be a new list with the specified items.
```
lis1= ["Nice","Appele",5,"54",8,"Me"]
lis2 = lis1[:] # lis2 is a new list
lis3 = lis1 # we didnt specify the range for lis1
lis3[0]="ok" #lis3 is a refernce to lis1
print(lis1,lis2,lis3) # the change also will occure in lis1
```

## Change a Range of Item Values
To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

```
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
```

### Note
If you insert more or less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly<br>
Thats due to the flexibilty of the lists :
```
thislist1= ["apple", "banana", "cherry"]
thislist2= ["apple", "banana", "cherry"]
thislist1[1:3] = ["watermelon"]
thislist2[1:2] = ["blackcurrant", "watermelon"]
print(thislist1,thislist2)
```
We can also use insert method to add new element into specific index, or append to element directly to the end of the list:
```
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
thislist.append("orange")
print(thislist)
```
to append more than one item use extend method
```
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
```
## Remove list items

The remove() method removes the specified item.
<code> thislist.remove("banana")</code><br>
The pop() method removes the specified index (if not specified it will remove the last item).
<code> thislist.pop()</code><br>
The del keyword also removes the specified index:
<code>del thislist[0]</code><br>
The clear() method empties the list. <code>thislist.clear()</code>

## Common List Methods

<ul>
        <li>append()    Adds an element at the end of the list</li>
        <li>clear()     Removes all the elements from the list</li>
        <li>copy()      Returns a copy of the list</li>
        <li>count()     Returns the number of elements with the specified value</li>
        <li>extend()    Add the elements of a list (or any iterable), to the end of the current list</li>
        <li>index()     Returns the index of the first element with the specified value</li>
        <li>insert()    Adds an element at the specified position</li>
        <li>pop()       Removes the element at the specified position</li>
        <li>remove()    Removes the item with the specified value</li>
        <li>reverse()   Reverses the order of the list</li>
        <li>sort()      Sorts the list</li>
</ul>

# Tuples
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.<br>
Tuples are collection which is ordered and unchangeable and allow duplicate values.
<br>
define a tuple:
<code>
  thistuple0= ("apple", "banana", "cherry")
  thistuple1= ("apple",)
  thistuple2= tuple(["nice","whather"])
</code>

### Typles Methods
Python has two built-in methods that you can use on tuples.
<ul>
        <li>count()     Returns the number of times a specified value occurs in a tuple</li>
        <li>index()     Searches the tuple for a specified value and returns the position of where it was found</li>
</ul>

# Sets
Sets are used to store multiple items in a single variable.<br>

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.<br>

A set is a collection which is unordered, unchangeable*, and unindexed.<br>
Note: Set items are unchangeable, but you can remove items and add new items. that means A set itself may be modified, but the elements contained in the set must be of an immutable type.<br>
Create a Set:<br>
<code>
  thisset = {"apple", "banana", "cherry"};
  thisset1= set(["apple", "banana", "cherry"]);
  print(thisset,thisset1)
</code>


### Add Sets

```
thisset = {"apple", "banana", "cherry"}
thisset.add("orange") # add the orange item to thisset
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical) # combine the two sets

```


### Common Set Methods
<ul>
        <li>add()       Adds an element to the set</li>
        <li>clear()     Removes all the elements from the set</li>
        <li>copy()      Returns a copy of the set</li>
        <li>difference()        Returns a set containing the difference between two or more sets</li>
        <li>difference_update() Removes the items in this set that are also included in another, specified set</li>
        <li>discard()   Remove the specified item</li>
        <li>intersection()      Returns a set, that is the intersection of two other sets</li>
        <li>intersection_update()       Removes the items in this set that are not present in other, specified set(s)</li>
        <li>isdisjoint()        Returns whether two sets have a intersection or not</li>
        <li>issubset()  Returns whether another set contains this set or not</li>
        <li>issuperset()        Returns whether this set contains another set or not</li>
        <li>pop()       Removes an element from the set</li>
        <li>remove()    Removes the specified element</li>
        <li>symmetric_difference()      Returns a set with the symmetric differences of two sets</li>
        <li>symmetric_difference_update()       inserts the symmetric differences from this set and another</li>
        <li>union()     Return a set containing the union of sets</li>
        <li>update()    Update the set with the union of this set and others</li>
</ul>

# Dictionary
Dictionary are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

Create and print a dictionary:
<code>
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
</code>
 
 ### Comman Dictionary methods
Python has a set of built-in methods that you can use on dictionaries.
<ul>
        <li>clear()     Removes all the elements from the dictionary</li>
        <li>copy()      Returns a copy of the dictionary</li>
        <li>fromkeys()  Returns a dictionary with the specified keys and value</li>
        <li>get()       Returns the value of the specified key</li>
        <li>items()     Returns a list containing a tuple for each key value pair</li>
        <li>keys()      Returns a list containing the dictionary's keys</li>
        <li>pop()       Removes the element with the specified key</li>
        <li>popitem()   Removes the last inserted key-value pair</li>
        <li>setdefault()        Returns the value of the specified key. If the key does not exist: insert the key, with the specified value</li>
        <li>update()    Updates the dictionary with the specified key-value pairs</li>
        <li>values()    Returns a list of all the values in the dictionary</li>
</ul>





You are here: 
https://pythonnumericalmethods.berkeley.edu/notebooks/chapter03.06-Summary-and-Problems.html#problems
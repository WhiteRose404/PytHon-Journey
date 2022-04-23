# PytHon-Journey
Python Journey is a simple, straight-forward programming course 👨‍💻 that will help you become comfortable programming in Python 3 🐍 and Beyond 🚀. This course built while i was studying for the python exam, since we didnt have a structure document for the course 💩, so this course was intended for me and my collegs at ENSIAS to help them pass with great success 🎉,


## Table Of Contents
1. [ Installation ](#installation)
2. [ Basic Operation. ](#basic-operation)
3. [ Lists. ](#Lists)
4. [ Tuples. ](#Tupless)
5. [ Sets. ](#Sets)
6. [ Dict. ](#Dict)
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

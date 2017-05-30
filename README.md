# NYPL Digital Collections API demo

### Sean Crowe, Carolyn Hansen - UC Libraries

## Scope and Purpose
We're going to go through the basic concepts of Python programming, using the script built upon example code from NYPL, to extract some key bibliographic data from the NYPL Collections API. We'll see how to apply this script to current data and how to modify it to access other data points.

## Setup
We'll be using Python __3__
* For Windows, Mac, and Linux, download from [Python.org/downloads](https://www.python.org/downloads/) and make sure to check `add to path` option on install.
* Once python3 is installed, install the requets module with pip ```pip3 install requests```

Test
1. With text editor, open a file and type ```print('hello world')``` and save it in your home directory as hello.py
1. In the windows command prompt (cmd.exe) or Mac terminal, cd to your home directory and type ```python3 hello.py``` You should see the output of the program.

NYPL API token
1. Get token [here](http://api.repo.nypl.org/). Also make note of your username and password for api calls from the web browser.

# Concepts

## Types

### Strings
*Strings are immutable*

* length  
```python  
len("Let's find the length of this string")
#>> 36
```
* concatenate  
```python  
"Hello " + "World"
#>> "Hello World"
```
* indexes 
```python
"Let's find a substring!".find("sub")
#>> 13
```

* regular expressions
```python
re.sub("a", "b", "I'm replacing all my a's with b's")
#>> "I'm replacing all my b's with b's"
```

* interpolation
```
page_number = '4'
print "Please turn to page {0}".format(page_number)
#>>> Please turn to page 4
```

### Integers
```
1 + 1
#>>> 2
```

* [range](https://docs.python.org/3/library/stdtypes.html#range)
```
list(range(10)
#>>>  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
## Variables
* assigning  
```python  
my_variable = "some string"
#>> "some string"
```

## File I/O
* readers & writers

## Loops
 
* [with](https://docs.python.org/3/reference/compound_stmts.html#with)
  Common method of *setting things up* for run time and closing out when job is finished
* for
```
matches = ['a', 'b', 'c']
for match in matches:
  print(match)
#>>> 
a
b
c
```

## Functions
* passing variables to functions as parameters

* return value
```python
def chop(i):
  for letter in i:
    print(letter)
  return 'yeah!'
var = 'heck'
chop(var)
#>>
h
e
c
k
"yeah!"
```
## Modules

* csv
* requests
* xmltree

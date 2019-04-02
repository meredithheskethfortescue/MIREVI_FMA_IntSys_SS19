# Introduction to Python

![](https://imgs.xkcd.com/comics/python.png)

[TOC]

## General FAQ

### Installation

#### Windows

[Download Python3](https://www.python.org/downloads/windows/) When installing check "Add Path Variable".
[Download PyCharm (Community Edition)](https://www.jetbrains.com/pycharm/download/#section=windows)



#### Linux

```bash
# install PyCharm IDE via snap package manager
sudo snap install pycharm-community --classic

# python3 is shipped with the most linux distributions so 
# you DON'T NECESSARILY NEED TO INSTALL python. You can use your system's interpreter. 
# If this should not be the case:
sudo apt-get install python3.7-dev
# IMPORTANT NOTE: When using your system's interpreter NEVER update your pip. 
# This might cause many problems with your OS!
```

#### MAC

[Download Python3](https://www.python.org/downloads/mac-osx/) or get it with *brew*.
[Download PyCharm (Community Edition)](https://www.jetbrains.com/pycharm/download/#section=mac)



### Most important shortcuts in PyCharm

| Shortcut                 | Effect                                   |
| ------------------------ | ---------------------------------------- |
| `Ctrl + P`               | Show possible arguments                  |
| `Ctrl + Space`           | Autocomplete                             |
| `Ctrl + Alt + L`         | Apply code conventions                   |
| `Ctrl + 5`               | Run                                      |
| `Ctrl + B`               | Go to declaration/implementation         |
| `Shift + F6`             | Refactoring                              |
| `Ctrl + D`               | Insert copy of the line to the next line |
| `Ctrl + Shift + Up/Down` | Move line upwards/downwards              |



### Why Python?

- Interpreted High-Level Language
    - Procedural
    - Object-oriented
    - Functional
    - Imperative
- 'Pythonic' design philosophy
    - [PEP 20 - The Zen of Python](https://www.python.org/dev/peps/pep-0020/)
    - [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- Cross-platform
    - Linux, Unix, Windows, Android, iOS
    - ARM architecture (e.g. [Raspberry Pi](https://www.raspberrypi.org/), [NVIDIA Jetson](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-nano/), [MicroPython on pyboard](https://micropython.org/))
- Use case:
    - De facto standard for Machine Learning, Neural Nets (e.g. [Tensorflow](https://www.tensorflow.org/), [PyTorch](https://pytorch.org/), [Caffee](http://caffe.berkeleyvision.org/))
    - Data Mining (Alternative to R)
    - Scientific Computing 
        (Alternative to Matlab by importing `numpy` and `matplotlib`; see [NumPy for Matlab users](https://docs.scipy.org/doc/numpy/user/numpy-for-matlab-users.html))
    - Web (e.g. Django)
    - Frontend (e.g. Qt, Tkinter)

### Python 2.7 and Python 3.x

Python 2.7 wird immernoch oft verwendet, da viele ältere Projekte noch darauf basieren, aber im Januar 2020 wird der Support eingestellt. **Wir verwenden hier deshalb ausschließlich Python 3!**
Python 3 ist **nicht vollständig abwärtskompatibel**. In vielen Foreneinträgen sind Beispiele und Lösungen zu finden, die unter Python 3 nicht funktionieren - Finger weg davon! Es sollte stets auf die Version geachtet werden, die gerade behandelt wird.
Die auffäligsten Unterschiede im Code, die direkt ins Auge springen sind folgende:

```python
# Python 2.7
print "'print' is a keyword without brackets and integers need a cast " + str(42)

# Python 3.x
print("'print' is a function that", "can concatenate multiple strings", "comma seperated",
     "and numbers like", 42, "are okay too.")

# Python 2.7 only: It is possible to import some newer features from Python 3 with this statement
from __future__ import *
```


### pip3 (pip installs package)

pip3 ist ein Paketverwaltungsprogramm, mit dem schnell und bequem Python-Bibliotheken per Konsolenbefehl installiert werden können.

```bash
# install numpy packages for python3 via pip 
# (for windows use only 'pip')
pip3 install numpy

# if a requirement file is provided by a repository it can be used to install the required packages automatically
pip3 install -r requirements.txt
```


### Python Console and Jupyter Notebook

Python kann (ähnlich wie Matlab) aus der Konsole heraus aufgerufen werden. Dies eignet sich zwar gut zum Testen und Zeigen von Beispielen, aber nicht zur Softwareentwicklung, weshalb diese Methode hier nicht vertieft werden soll.

```python
>>> import numpy as np
>>> example = np.array([3,4,5])
>>> print("My example array looks like", example)
My example array looks like [3 4 5]
```

Jupyter Notebook verfolgt dagegen den Ansatz, kleinere Codeblöcke im Browser darzustellen und in eine Art Dokumentation einzubinden. Dies ist gut für Forschung und Lehre, aber ebenfalls nicht zur Entwicklung umfangreicherer Projekte geeignet.



## Python Syntax Crashkurs

### Hello, world!

```python
print("Hello, world!")
```

By the way: Python is case sensitive!

### Comments

```python
"""I'm a Docstring
Docstrings support multiple lines and are invoked with three double quotes.
"""

'''Multiline comments
Invoked with three single quotes.
'''

# simple comment with a hash
```




### Variable types

```python
'''Datatypes must not be specified explicitly - in python they are dynamic.
This means that a variable can change it's datatype if necessary.
'''
## ATOMIC DATATYPES
# initialize x as integer
x = 5
# overwrite x with a float
x = 1.2
# overwrite x with a string
x = "Hello, world!"
# bool
x = True
x = False

## COLLECTIONS
# lists are sorted sets of values
my_list = [3.14, 2.71, 'foo', 42, [4, 2], 9]  # list can contain floats, strings and integers and another list
my_list.append(0.29)  # add a new element to the list
my_list += ['bar']  # short hand for appending to lists is the '+' operator
print(my_list[0])  # prints the first item of the list: '3.14'

# tuples are like lists, but they are immutable
my_tuple = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print(my_tuple[1:3]) # prints ('bar', 'baz')

# dictionarys are unsorted sets. They link a key to a value.
my_dict = {'pi': 3.14,
           'e': 2.71}
my_dict['sqrt_2'] = 1.41  # add a new entry to the dictionary
print(my_dict['pi'])  # get a dictionary's entry by it's key
```

### Operators

```python
print(2+3)      # 5             addition
print(3*4)      # 12            multiplication
print(2**10)    # 1024          power
print(7/3)      # 2.33333333333 division
print(7//3)     # 2             integer division
print(7%3)      # 1             modulo division

i += 1  # increment (i++ is not possible in python)
```


### Loops and Conditions

```python
# instead of {curved brackets} python uses indentation (with 4 spaces)
if x > 5:
    print("Hello, world!")
    print("Everything indented will be in the condition")
    
print("This is not indented anymore so it does not care about the if condition.")


if some_kind_of_boolean_flag:
    print("I'm in the if-condition!")
elif y == 9:
    print("I'm in the else-if-condition!")
else:
    print("I'm in the else-condition!")

    
while x <= 42 or x == 4711:
    print(x)
    x += 1

    
# For loops in python need an iterable to loop over like a list or array.
my_list = [2, 4, 6, 8]
for it in my_list:
    print(it)
    
# The 'range' and function can provide such an iterable.
# 'range(10)' gives 0..9
for it in range(10):
    print(it)

# The 'range' function provides further optional parameters to declare start and stepwidth.
# To see, what arguments a function can take, use the 'Ctrl + P' shortcut of PyCharm!
for it in range(2, 2048, 8):
    print(it)

# The 'enumerate' function provides the elements of a list or array and counts them
for index, element in enumerate(my_list):
    print(index, element)
```



## Basic Slicing and Indexing

```python
# create a python list
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# access single values by index
print(lst[5])    # 5
print(lst[-1])   # 9 --> negative numbers count backwards from the end

# you can access a subset by slicing in the form of [start:end]
print(lst[2:6])  # [2, 3, 4, 5]          --> all values from index 2 to 6 (exclusive)
print(lst[5:])   # [5, 6, 7, 8, 9]       --> no end given means take all to the end
print(lst[:-3])  # [0, 1, 2, 3, 4, 5, 6] --> all up to the last three values
```



### Methods and functions

```python
# PEP 8: Function names should be lowercase, with words separated by underscores 
# as necessary to improve readability.
def my_function(a, b):
    sigma = a + b
    return sigma

# call function with arguments
c = my_function(2, 3)


# A function can have positional arguments and optional arguments with default values
def analyze_array(array, start=0, end=None):
    sigma = sum(array[start:end])
    mean = sigma / len(array[start:end])

    # A function can have multiple return values
    return sigma, mean


my_list = [2, 4, 6, 8]
# multiple return values are written comma seperated
sum_all, mean_all = analyze_array(my_list)  # call function without optional args
sum_some, mean_some = analyze_array(my_list, end=-1)  # call function with optional args

print(sum_all, mean_all)
print(sum_some, mean_some)
```



### Exercise: Prime numbers

Schreiben Sie ein skript, das...

- ...alle Primzahlen von 2 bis 1000 in einer Liste speichert.
- ...die 12. Primzahl ausgibt.



### Classes

```python
# PEP 8: Class names should normally use the CapWords convention.
class MyClass:
    def __init__(self, a, b):
        """Constructor"""
        self.a = a
		self.b = b
        
    def multiply(self):
        return self.a * self.b

    def pythagoras(self):
        return math.sqrt(self.a ** 2 - self.b ** 2)

    def set_values(self, a, b):
        self.a = a
        self.b = b


# get new instance
my_instance = MyClass(a, b)

# call its functions
print(my_instance.pythagoras())
my_instance.set_values(7, 13)
```




## import package

Eine der größten Stärken von Python liegt in den Bibliotheken, die für die meisten Problemstellungen bereits vorgefertigte Funktionen bieten.
Wie bereits erwähnt, kann mit Pip3 ein benötigtes Paket schnell installiert, und mit der import Funktion sofort verwendet werden:

```bash
# install needed packages in your operating system terminal
# (for windows use only 'pip')
pip3 install numpy
```

```python
# in your python file import the package with the namespace of your choice
import time

import tqdm
import numpy as np

# and you can use them
my_numpy_array = np.array([[1, 2, 3],
                           [4, 5, 6]])

my_numpy_array_reshaped = np.reshape(my_numpy_array, [np.size(my_numpy_array)])

for element in tqdm.tqdm(my_numpy_array_reshaped, desc="Waiting"):
    time.sleep(element)
```

| Die wichtigsten Standardbibliotheken |                                                              |
| ------------------------------------ | ------------------------------------------------------------ |
| os                                   | Operating System. Dateien öffnen/speichern, Dateipfade, etc. |
| sys                                  | Zugriff auf den verwendeten Python Interpreter               |
| math                                 | Mathematische Operationen und Konstanten                     |
| time                                 | Timer, Wartezeiten, etc.                                     |
| timeit                               | Performancetesting von kurzen Codeabschnitten                |
| argparse                             | Parsen von Argumenten beim Kommandozeilenaufruf              |

| Die wichtigsten third party packages |                                                              |
| ------------------------------------ | ------------------------------------------------------------ |
| numpy                                | Performante Berechnungen und bequeme Handhabung von <br />Vektoren, Matrizen, mehrdimensionalen Matrizen und generellen <br />numerischen Operationen |
| pandas                               | Performanter Zugriff auf komplexe Datenstrukturen.<br />Beispielsweise import von `*.csv` Dateien. |
| matplotlib                           | Grafische Darstellung von Daten und mathematischer Funktionen |
| scipy                                | Lineare Algebra, numerische Integration, Interpolation, FFT, <br />Signalverarbeitung, Bildverarbeitung |



### Lokale Imports
Um Codeteile zu kapseln und wiederverwendbar zu gestalten, kann jedes Python Skript als Modul importiert werden.


Angenommen die beiden Dateien `main.py`  und `utils.py` befinden sich im gleichen Ordner.


```python
# this is the python utility file 'utils.py'
# defined functions and globals can be used by other files when imported
GLOBAL_STRING_EXAMPLE = "dubidubida"

def fancy_function():
    print("fancy")

def knowing_function():
    print(42)

if __name__ == '__main__':
    # this will only be executed if this file is executed (not imported)
    fancy_function()
    knowing_function()
```

```python
# this is the python main file 'main.py'
import utils  # import local python file

print(utils.GLOBAL_STRING_EXAMPLE)  # use imported file as module
utils.fancy_function()
```



## Matplotlib

Das Standardtool zum plotten von mathematischen Funktionen oder Daten ist Matplotlib.

```python
import matplotlib.pyplot as plt

# add a scatter plot
dataset_0 = [1, 10, 12, 0.5, 4, 3, 2, -3]
plt.scatter(list(range(len(dataset_0))), # values for x axis
            dataset_0)  # values for y axis

# add a function plot
dataset_1 = []
for it in range(8):
    dataset_1 += [it ** 2]

plt.plot(dataset_1)

# show plot window
plt.show()
```

### Exercise: Plot Collector

1. Erstellen Sie eine Liste mit Werten (Datensatz)
2. Plotten Sie diesen mit matplotlib
3. Erstellen Sie eine Klasse, die...
    1. ...mehrere Datensätze enthalten kann.
    2. ...eine Möglichkeit bietet, weitere Datensätze hinzuzufügen
    3. ...eine Möglichkeit bietet, alle gesammelten Datensätze in einem Plot darzustellen.
    4. ...eine Möglichkeit bietet, die Anzahl der aktuell hinzugefügten Datensätze auszugeben

### Exercise: Performance Optimization

Sum of multiples of two numbers
If we list all the natural numbers below 10 that are multiples of 3 or 5
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of a or b below n.
When you found your first solution, think again how exactly the described sequence of numbers works.
Try to find a pattern and how you could design an algorithm to speed up the calculation time.




## Numpy Syntax

Numpy vereint die komfortable Syntax von Python mit der Performanz von C. Es handelt sich um eine in C geschriebene und kompilierte Bibliothek. Kernelement ist die Datenstruktur `ndarray` welche im Hintergrund als C- oder Fortranarrays erzeugt werden.
Numpy ermöglicht komfortables und schnelles Durchführen numerischer Operationen mit n-dimensionalen Matrizen (ähnlich wie Matlab). Der wesentliche Geschwindigkeitsboost entsteht hier durch das Vermeiden von for-Schleifen. Stattdessen sollten die numpy-internen Funktionen verwendet werden, welche die Operation dann direkt auf das ganze Array anwendet.

### n-dimensionales Indexing / Slicing mit numpy

```python
# numpy can handle multidimensional arrays
import numpy as np

# syntax for a 2d array is like an array of arrays
arr_2d = np.array([[0, 1, 2],
                   [3, 4, 5]])

print(arr_2d[1, 2])   # 5
print(arr_2d[:, 1])   # [1, 4] --> ':' means all values of that axis

# same for 3d array (more than three are possible too)
arr_3d = np.zeros([2, 3, 4])  # create 2x3x4 array filled with zeroes
arr_3d[1, 1, 1] = 1
print(arr_3d)                 # [[[0. 0. 0. 0.]
                              #   [0. 0. 0. 0.]
                              #   [0. 0. 0. 0.]]
                              #
                              #  [[0. 0. 0. 0.]
                              #   [0. 1. 0. 0.]
                              #   [0. 0. 0. 0.]]]
```

![](./img/anatomyarray_exposed.png)

### Operationen in Numpy

```python
# Numpy arrays aren't lists! Lists are Stack-like collections.
my_list = [0, 1, 2]
print(my_list * 2)  # prints [0, 1, 2, 0, 1, 2] --> instead of multiplication the list is concatenated with itself

# Numpy arradot_productys are made for numeric operations:
my_nparray = np.array([0, 1, 2])
print(my_nparray * 2)  # prints [0, 2, 4] --> Multiplication

# Numpy gets fast by avoiding for loops. Instead it's own functions should be prefered.
# For example:
shape = np.shape(arr_2d)  # Gives the dimensions as tuple: (2, 3)
size = np.size(arr_2d)  # Gives the number of elements: 6
 = np.dot(arr_2d, [1, 2, 3])  # Dot product of two arrays: array([8, 26])
```



## Ich möchte noch mehr machen, weiß aber nicht was!

- Weitere Zahlenprobleme finden sich unter [projecteuler.net](projecteuler.net)
- Image Processing
    - Weiterer Filter zur Kantenerkennung: Laplace of Gaussian
        Hier kann mit der Kernelgröße experimentiert werden. 
        Mit `generic_filter `können auch andere Berechnungen als die Summe implementiert werden, um andere Effekte zu erzielen.
    - Mit dem `argparse` Modul kann ein Commandline Interface erstellt werden.
        Damit können Ein- und Ausgabepfade sowie Flags (z.B. für Hellen/Dunklen Hintergrund) gesetzt werden.
        Befehle für die Pfadangaben finden sich in `os.path`.

## References

- http://pages.physics.cornell.edu/~myers/teaching/ComputationalMethods/python/anatomyarray.png
- https://imgs.xkcd.com/comics/python.png

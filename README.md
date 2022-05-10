# Class List
A Python program by Terry Kariuki

# Description
A python program that takes in 5 students and enters marks of 4 subjects, calculates their averages and ranks them into descending order.

# Usage
```python
import pandas as pd
import operator

#data to be used
data = {'Name': ['Terry','Victor','Brian','Ivy','Essy'],
        'Maths': [70,31,60,90,80],
        'English': [100,46,65,60,56], 
        'Kiswahili': [30,52,29,80,40],
        'Science': [43,28,37,55,34]
        }

#retrieve the data values and store them
stdName = data.get("Name")
mathsU = data.get("Maths")
EnglishU = data.get("English")
KiswahiliU = data.get("Kiswahili")

#store the average score of students in a dictionary
avg_score = {}

# iterate through a loop to get the average score of the students
for i in range(len(mathsU)):
    name = stdName[i]
    average = ( mathsU[i] + EnglishU[i] + KiswahiliU[i])//3
    avg_score[name] = average

# rank the students in descending order
sorted_x = sorted (avg_score.items(),key=operator.itemgetter(1),reverse=True)
print(sorted_x)
```

# Author
[Terry-Kariuki] (https://github.com/TERRYYYY)

# Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. 

# Getting Started
## Dependancies
Windows 10

## Installing
#### Step 1: Download Python
To start, go to [python downloads](python.org/downloads) and then click on the button to download the latest version of Python.

#### Step 2: Run the .exe file
Next, run the .exe file that you just downloaded, and then follow the installation instructions.

## Executing Program
Run python3 (name of file) ie ```
python3 classList.py ```

# Technology Used
Python

# Support and Contact
Email : kariuki.terry11@gmail.com

## License
[MIT](https://choosealicense.com/licenses/mit/)

import pandas as pd
import operator

data = {'Name': ['Terry','Victor','Brian','Ivy','Essy'],
        'Maths': [70,55,60,45,80],
        'English': [100,75,65,60,90], 
        'Kiswahili': [30,60,45,45,40]
        }

stdName = data.get("Name")
mathsU = data.get("Maths")
EnglishU = data.get("English")
KiswahiliU = data.get("Kiswahili")

avg_score = {}

for i in range(len(mathsU)):
    name = stdName[i]
    average = ( mathsU[i] + EnglishU[i] + KiswahiliU[i])//3
    avg_score[name] = average

sorted_x = sorted (avg_score.items(),key=operator.itemgetter(1),reverse=True)

print(sorted_x)
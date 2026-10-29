"""Q4: Update student marks in list"""
import json
try:
    with open('students.json') as f: data=json.load(f)
    roll=input('Roll: ')
    for s in data:
        if s['roll']==roll: s['marks']=float(input('New marks: ')); break
    else: print('Roll not found')
    with open('students.json','w') as f: json.dump(data,f,indent=2)
except FileNotFoundError: print('Run Q01 first')

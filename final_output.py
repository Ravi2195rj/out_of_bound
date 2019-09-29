import json
from collections import OrderedDict
import ast
import pickle as pk
with open(r"someobject.pickle", "rb") as input_file:
    result = pk.load(input_file)

json_dict = []
for question in result:
    flag  = 0
    for x in json_dict:
        if x['text']==question['Sentence'].strip()+".":
            flag = 1
            x['fibs'].append(question['Answer'].strip())
    if flag == 0:
        empty_dict = OrderedDict() 
        empty_dict['text'] = question['Sentence'].strip()+"."
        empty_dict['fibs'] = [question['Answer'].strip()]
        json_dict.append(empty_dict)

final_op = json.dumps(json_dict)
#print(final_op)
final_op = final_op[1:-3]
for x in final_op.split(']}, '):
    print x + "]}"

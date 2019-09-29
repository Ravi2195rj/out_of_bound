import json
import re
Original_Output_File = '11_chemistry_3.json'
Model_Generated_Output_File = 'submit.json'

Original_Output = []
Model_Generated_Output = []
Actual_Sentences = []
Model_Generated_Sentences = []
Match = 0

with open(Original_Output_File, encoding='utf-8-sig') as text:
    Original_Output = text.readlines()
    for Line in Original_Output:
        Line = Line.rstrip().lower().strip()
        Line = json.loads(Line)
        Text = Line['text']
        if Text not in Actual_Sentences:
            Actual_Sentences.append(Text)

with open(Model_Generated_Output_File, encoding='utf-8-sig') as text:
    Model_Generated_Output = text.readlines()
    for Line in Model_Generated_Output:
        Line = Line.rstrip().lower().strip()
        Line = json.loads(Line)
        Text = Line['text']
        if Text not in Model_Generated_Sentences:
            Model_Generated_Sentences.append(Text)
        if Text in Actual_Sentences:
            Match += 1
        


# print(Match)
TP = Match
FN = len(Actual_Sentences) - Match

Recall = TP / (TP + FN)
Precision = TP / len(Model_Generated_Sentences)
F1 = 2 * (Precision * Recall) / (Precision + Recall)

print("F1 score:", F1)
print("Precision", Precision)
print("Recall", Recall)

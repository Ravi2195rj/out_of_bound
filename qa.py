from select1 import SentenceSelection
from gap_selection import GapSelection
from copy import deepcopy
import re
import pickle as pk
sc = SentenceSelection()
f = open('chapter.txt')
list_of_lines = f.readlines()
list_of_lines = '\n'.join(list_of_lines)
f.close()
new_list_of_lines = []
list_of_lines = re.split('\.', list_of_lines)



for sentno , sent in enumerate(list_of_lines):
    if(len(sent.split(' ')) <= 4):
        continue
    org_sent  = deepcopy(sent)
    sent  = sent.lower()
    
    sent = sent.replace("fig","").strip()
    
    if ("exercise" in sent or "summary" in sent ) and sentno > 50:
        break
    if(len(sent) > 0 and sent[0].isdigit() == True  ):
        continue
    if('?' in sent or '=' in sent or len(sent) < 15 or sent[0] == '('):
        continue
    org_sent  = org_sent.replace('\t',' ').strip()
    org_sent = re.sub(r'[^\x00-\x7F]+','', org_sent)

    new_list_of_lines.append(org_sent.strip())

data = ".".join(new_list_of_lines )

#print new_list_of_lines
#op = sc.prepare_sentences_from_rawtext(f)
f = open('temp.txt', 'w')
f.write(data)
f.close()
op = sc.prepare_sentences('temp.txt')
# for key in op:
#     print op[key]
gs = GapSelection()

sentences = []
for s in op:
    if len(op[s]) > 10:
	#print 'Selected sentence:', op[s]
	sentences.append(op[s] )
        #print '\n'
print(op.values())
result = gs.get_candidates(op)
f = open("temp_ans.txt","w+")
f.write(str(result)[1:-1] )
with open(r"someobject.pickle", "wb") as output_file:
    pk.dump(result, output_file)
with open(r"someobject.pickle", "rb") as input_file:
    result = pk.load(input_file)
#print type(result)
for questions in result:
    print "question: " + questions['Sentence'] 
    print "Fib: " +  questions['Answer']


import re
import requests
input_file = open("hp5.txt", "r")
text = ""

for line in input_file: 
  line = line.strip() 
  text += line + " "
  
result = re.findall("(whispered ([A-Z]\w+ [A-Z]\w+|[A-Z]\w+)|([A-Z]\w+ [A-Z]\w+|[A-Z]\w+) whispered)", text)
whisps = []

for i in range(len(result)): 
  for k in range(len(result[i])): 
    if result[i][k]: 
      whispered = re.findall("(whispered \w+|\w+ whispered)", result[i][k]) 
        if whispered: whispers = re.findall("[A-Z]\w+", whispered[0]) 
        whisps = whisps + whispers
        
  def uniq(input): 
    output = [] 
    for x in input: 
      if x not in output: 
        output.append(x) 
    return output
          
  Max = []
  
  w_set = uniq(whisps)
  
  for i in range(len(w_set)): 
    N = 0 
    for k in range(len(whisps)): 
      if w_set[i] == whisps[k]: 
        N += 1 
    Max.append(N)
    
  for i in range(len(Max)): 
    if Max[i] == max(Max): 
      print(max(Max), w_set[i])

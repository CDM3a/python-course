input_file = open("yazkora.txt", "r")

text = ""
for line in input_file:
    line = line.strip()
    text += line

sentences = text.split(".")


words = ""

for i in range(len(sentences)):
    words = sentences[i].split(" ")
    for k in range(len(words)):
        ending = words[k]
        END = ending[-1] + ending [-2]
        if END == "yo":
            print (ending)

#Надо убрать пробелы при считывании в предложения и доделать цикл, но не успел




input_file = open("yazkora.txt", "r")
answer = open("answer.txt", "w")

text = ""
for line in input_file:
    line = line.strip()
    text += line + " "

sentences = text.split(".")

for i in range(len(sentences)):
    if sentences[i] == "":
        del sentences[i]

for i in range(len(sentences)):
    SNTC = sentences[i].strip()
    words = SNTC.split(" ")
    out_sent = ""
    for k in range(len(words)):
        word = words[k]
        ending = word[-2:]
        if ending == "yo":
            out_sent += word + " "
    answer.write(out_sent + "\n")

input_file.close()
answer.close()






input_file = open('dict.txt', "r")

text = ''
for line in input_file:
    text += line.strip() + "\n"

dict = text.split("\n")


adjective = ''
noun = ''
verb = ''

for word in dict:
    if word.endswith('yo'):
        adjective += word + " "
    elif word.endswith('ka'):
        noun += word + " "
    else:
        verb += word + " "

adjective = adjective.split()
noun = noun.split()
verb = verb.split()

comb_noun_verb = len(noun)*len(verb)
comb_adj = len(adjective)


def factorial(x):
    F = 1
    for i in range(1, x + 1):
        F *= i
    return(F)

def combinations(n, k):
    if k > n:
        return 0
    elif n == k or k == 0:
        return 1
    else:
        return (factorial(n)/(factorial(k)*factorial(n-k)))

combination = 0

if comb_adj < 8:
    for i in range(1, comb_adj+1):
        combination += combinations(comb_adj, i)
else:
    for i in range(1, 8):
        combination += factorial(comb_adj) / combinations(comb_adj, i)


out = int(combination * comb_noun_verb)
print(out)

import random

inText = "S. 110-125\nS. 265-281"

word = " "
spacer = "\t"

def strsec(inText, word, spacer, decal, decalLetters):
    out = ""

    for char in inText.encode('ascii'):
        for c in range(char):
            if decal == True:
                while True:
                    out += random.choice(decalLetters)

                    if random.random() > 0.5:
                        break
                
            out += word

        out += spacer
    
    return out

def strenc(outText, word, spacer):
    out = ""
    counter = 0

    for i in range(len(outText)):
        char = outText[i]
        if char == word:
            counter+=1
        if char == spacer:
            out += chr(counter)
            counter = 0
    
    return out

decalLetters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!\"§$%&/()=?"
out = strsec(inText, word, spacer, False, decalLetters)
print(out)

result = strenc(out, word, spacer)
print(result)

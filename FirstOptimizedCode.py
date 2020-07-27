def sentence_maker(phrases):
    questions=("how","where","when","why","what")
    capitalized = phrases.title()
    if phrases.startswith(questions):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)
print(sentence_maker("what are you"))

total=[]
final=''
while True:
    message=input("Say Something:")

    if message == "\end":
        break
    else:
        total.append(sentence_maker(message))
        continue
print(" ".join(total))


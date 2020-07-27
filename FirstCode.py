total=[]
while True:
    message=input("Say Something:")
   
    if message == "\end":
        final=''
        for msg in total:
            if msg.find("How") == -1 or msg.find("What") == -1:
                final=final+msg.title()+"."
            else:
                final=final+msg.title()+"?"

        print(final)
        break
    else:
        total.append(message)
        continue
def passwordcheck(pas):
    if isinstance(pas,str):
        if len(pas) < 8:
            return False
        else:
            return True

passwordcheck
def mean(value):
    if type(value) == dict:
        the_mean=sum(value.values())/len(value)
    else:
        the_mean=sum(value)/len(value)
    return the_mean

def meanone(value):
    if isinstance(value ,dict):
        the_mean=sum(value.values())/len(value)
    else:
        the_mean=sum(value)/len(value)
    return the_mean

print("ForDictionary",mean({"man":1,"can":2}))
print("ForList",mean([1,2,3,4]))

print("ForDictionary",meanone({"man":1,"can":2}))
print("ForList",meanone([1,2,3,4]))
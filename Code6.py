state_capital={"UP":"Lucknow","MP":"Bhopal","Rajasthan":"Jaipur"}
for st in state_capital.items():
    print(st)

for st in state_capital.keys():
    print(st)

for st in state_capital.values():
    print(st)

for key,value in state_capital.items():
    print("{} has capital {}".format(key,value))
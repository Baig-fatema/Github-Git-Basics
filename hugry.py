is_hugry=input("Are you hugry?")
if is_hugry.lower() == "yes":
    print("eat Samosa")
    print("eat Pizza")
else:
    thirsty=input("Are you thirsty:")
    if thirsty.lower() == "yes":
        print("Drink water")
    print("Do complete your homework")    
    


'''
undo uncommited changes : $ git checkout -- hugry.py
undo commmited changes : $ git revert commit id
reset : $ git reset commit id (from log history)
'''    
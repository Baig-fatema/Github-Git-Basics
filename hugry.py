is_hugry=input("Are you hugry?")
if is_hugry.lower() == "yes":
    print("eat Samosa")
    print("eat Pizza")
else:
    print("Do complete your homework")    
    


'''
undo uncommited changes : $ git checkout -- hugry.py
undo commmited changes : $ git revert commit id
reset : $ git reset commit id (from log history)

Branch :
git branch
git checkout new_branch name     (create new barch)
git log       (check commit history)
'''    
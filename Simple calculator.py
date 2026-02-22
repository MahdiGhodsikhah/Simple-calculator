#%%
def add (a,b) : return a+b
def minus (a,b) : return a-b
def divide (a,b) : return a/b
def multiply (a,b) : return a*b

dic = {"+":add,"-":minus,"/":divide,"*":multiply}

while True :
    a = int(input("Enter the first number: "))
    operator = input("Enter the operator: ").strip()
    b = int(input("Enter the second number: "))
    func = dic[operator](a,b)
    print(func)
    continue_or_not = input("Do you want to continue? (y/n)")
    if continue_or_not == "y" :
        continue
    else :
        break
# %%
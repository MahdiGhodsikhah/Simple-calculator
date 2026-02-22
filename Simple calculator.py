#%%
def add (a,b) : return a+b
def minus (a,b) : return a-b
def divide (a,b) : return a/b
def multiply (a,b) : return a*b

a = int(input("Enter the first number: "))
operator = input("Enter the operator: ")
b = int(input("Enter the second number: "))

dic = {"+":add,"-":minus,"/":divide,"*":multiply}

while True :
    func = dic[operator](a,b)
    print(func)
    continue_or_not = input("Do you want to continue? (y/n)")
    if continue_or_not == "y" :
        continue
    else :
        break
# %%
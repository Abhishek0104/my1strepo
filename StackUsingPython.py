stk = []
max = 10

def push(num):
    if len(stk) == max:
        print("\nSorry, cant insert element. It is full.")
    else:
        stk.append(num)
        print("\nCurrent Stack : ",stk)
        
def pop():
    if stk == [] :
        print("Sorry, cannot pop. It is empty.\n")
    else:
        #stk.pop(num)
        print("\nThe popped element: ",stk.pop(-1))
        print("\nCurrent Stack : ",stk)

for i in range(1,max):
    push(i)  
for i in range(0,max):
    pop()

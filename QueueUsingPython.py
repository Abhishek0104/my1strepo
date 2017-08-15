queue = []
max = 10

def push(num):
    if len(queue) == max :
        print("\nThe quuee is full")
    else:
        queue.append(num)
        print("\nCurrent queue: ",queue)

def pop():
    if len(queue) == 0:
        print("\nQueue is empty.")
    else:
        print("\nThe popped element is : ",queue.pop(0))
        print("Current queue: ",queue)
    
for i in range(0,max):
    push(i)
for i in range(0,max):
    pop()
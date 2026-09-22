stack=[]
def push():
    x=int(input("Enter element to push:"))
    stack.append(x)
def pop():
    if len(stack)==0:
        print("Stack is empty")
    else:
        print("Popped element:",stack.pop())
def display_stack():
    print("Stack:",stack)

queue=[]
def enqueue():
    x=int(input("Enter element to enqueue:"))
    queue.append(x)
def dequeue():
    if len(queue)==0:
        print("Queue is empty")
    else:
        print("Dequeued element:",queue.pop(0))
def display_queue():
    print("Queue:", queue)

n = int(input("Enter number of elements for stack:"))
for i in range(n):
    push()

display_stack()
push()
pop()
display_stack()
push()
n = int(input("\nEnter number of elements for queue: "))
for i in range(n):
    enqueue()

display_queue()
enqueue()
dequeue()
display_queue()
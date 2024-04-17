stack = []

#push 
stack.append(1)
stack.append(2)
stack.append(3)
print("stack:",stack)  #output [1,2,3]

#pop
num = stack.pop()
print("pop:",num) #output 3
How to write For-loop
#peek
topNum = stack[-1]
print("peek:",topNum) #output 2

#isEmpty
isEmpty = not bool(stack)
print("isEmpty:",isEmpty) #output False

#size 
print("size:",len(stack)) # output 2


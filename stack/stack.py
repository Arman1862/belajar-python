# Stack is an abstract data type which items just can added or deleted on in top side
# Work with LIFO method, last in first out
# so we can just delete items first that (were previously entered last)(yang sebelumnya dimasukkan paling terakhir)

# .push: add new item in the top
# .pop: delete item from the top

stack = []

def push(stack, item): # push is conceptual function
	stack.append(item)

def pop(stack):
	stack.pop()

stack = []
print(stack)
push(stack,"A") # adding item A
print(stack)
push(stack,"B") # adding item B
print(stack)
pop(stack) # deleting last element from the list -> elemen B
print(stack)
push(stack,"C") # adding item c
print(stack)
pop(stack) # deleting last element from the list -> elemen C
print(stack)
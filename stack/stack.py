# Stack is an abstract data type which(dimana) items just can
# added or deleted on in top side

# Work with LIFO method, last in first out
# so we can just delete items first that (were previously entered last)(yang sebelumnya dimasukkan paling terakhir)

# .push: add new item in the top
# .pop: delete item from the top

# stack = []

# def push(stack, item): # push is conceptual function
# 	stack.append(item)

# def pop(stack):
# 	stack.pop()


# stack = []
# print(stack)
# push(stack,"A") # adding item A
# print(stack)
# push(stack,"B") # adding item B
# print(stack)
# pop(stack) # deleting last element from the list -> elemen B
# print(stack)
# push(stack,"C") # adding item c
# print(stack)
# pop(stack) # deleting last element from the list -> elemen C
# print(stack)

# it's just default push and pop, why ewe make a new function
# well i don't know so you can just see this link, gemini explain why we must use that method
# https://gemini.google.com/share/727f48699883

# in class form(dalam bentuk class)
# more neater(rapi) and readable

class Stack:
	def __init__(self):
		self.stack = []

	def is_empty(self):
		return True if len(self.stack) == 0 else False

	def push(self, item):
		self.stack.append(item)

	def get_stack(self):
		return self.stack

	def pop(self):
		return None if self.is_empty() else self.stack.pop()

stack = Stack() # mendeklarasikan instance stack
print(stack.get_stack())
stack.push("A")
stack.push("B")
print(stack.get_stack())
print(stack.pop())
print(stack.get_stack())
print(stack.pop())
print(stack.get_stack())
print(stack.pop()) # harusnya menampilkan error karena stack sudah kosong
# abstract data types where data deletion is only possible
# from the front or initial sequence and additions are only 
# possible from the back sequence.

# newest added item will be deleted first because work with
# FIFO, first in first out

# enqueue: adds a new item to the back of the queue
# dequeue: removes a item from front of theb queue

# like antri mbg, first come first served

class Queue:
	def __init__(self):
		self.queue = []

	def is_empty(self):
		return True if len(self.queue) == 0 else False

	def get_queue(self):
		return self.queue

	def enqueue(self, item):
		self.queue.append(item)

	def dequeue(self):
		return None if self.is_empty() else self.queue.pop(0)
		# .pop(0) because first item is in index 0

queue = Queue() # initialize instance queue
print(queue.get_queue())
queue.enqueue("A")
queue.enqueue("B")
print(queue.get_queue())
print(queue.dequeue())
print(queue.get_queue())
print(queue.dequeue())
print(queue.get_queue())
print(queue.dequeue()) # must be display an error(none) because the list is empty
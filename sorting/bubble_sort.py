def bubble_sort(s):
	n = len(s)
	for i in range(n):
		print(s)
		for j in range(n - 1):
			if s[j] > s[j + 1]:
				s[j], s[j + 1] = s[j + 1], s[j]


my_list = [50, 30, 40, 10, 20]
print("list sebelum disortir", my_list)
bubble_sort(my_list)
print("list sesudah disortir", my_list)
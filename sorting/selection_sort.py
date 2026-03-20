def selection_sort(S):
	n = len(S)
	for i in range(n - 1):
		print(S)
		smallest = i
		for j in range(i + 1, n):
			if S[j] < S[smallest]:
				smallest = j

		S[i], S[smallest] = S[smallest], S[i]

S = [50, 30, 40, 10, 20]
print("list sebelum disortir", S)
selection_sort(S)
print("list sesudah disortir", S)
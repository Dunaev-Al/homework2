arr = [1, 2, 3, 4, 5, 6, 7]
length = len(arr) - 1
second_searcher = 0
new_arr = []

for first_searcher in arr[1::2]:
    new_arr.append(first_searcher)
    new_arr.append(arr[second_searcher])
    second_searcher += 2

new_arr.append(arr[length])

arr = new_arr
print(arr)


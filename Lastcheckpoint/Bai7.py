
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

original_list = [5, 1, 8, 92, -1, 30]
print("Original list:", original_list)
sorted_list = bubble_sort(original_list)
print("Sorted list:", sorted_list)
import random
import timeit
# creating a random array of number :
def create_random_array(length):
    arr = []
    for i in range(length):
        arr.append(random.randint(0, 1000))
    return arr

# comparing algorith : 
def sort_timer(arr):
    insertion_sort_time = timeit.timeit(lambda: insertion_sort(arr), number=100)
    merge_sort_time = timeit.timeit(lambda: merge_sort(arr), number=100)
    quick_sort_time = timeit.timeit(lambda: quick_sort(arr), number=100)
    bubble_sort_time = timeit.timeit(lambda: bubble_sort(arr), number=100)
    selection_sort_time = timeit.timeit(lambda: selection_sort(arr), number=100)



    times = {
        "Insertion Sort": insertion_sort_time,
        "Merge Sort": merge_sort_time,
        "Quick Sort": quick_sort_time,
        "bubble sort": bubble_sort_time,
        "selection sort" : selection_sort_time
    }

    fastest_sort = min(times, key=times.get)

    return fastest_sort

# selection sort function : 
def selection_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n):
        if reverse:
            max_index = i
            for j in range(i+1, n):
                if arr[j] > arr[max_index]:
                    max_index = j
            arr[i], arr[max_index] = arr[max_index], arr[i]
        else:
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

#  Bubble Sort function : 
def bubble_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if reverse:
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Insertion Sort functioon : 
def insertion_sort(arr, reverse=False):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        if reverse:
            while j >= 0 and key > arr[j]:
                arr[j+1] = arr[j]
                j -= 1
        else:
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr

# Merge Sort function :
def merge_sort(arr, reverse=False):
    if len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half, reverse)
        merge_sort(right_half, reverse)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if reverse:
                if left_half[i] > right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
            else:
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Quick Sort function :
def quick_sort(arr, reverse=False):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if reverse:
        return quick_sort(right, reverse=True) + equal + quick_sort(left, reverse=True)
    else:
        return quick_sort(left) + equal + quick_sort(right)



if __name__ == '__main__' : 
    araay_lenght = int(input ("enter n "))
    arr = create_random_array(araay_lenght)
    fastest_sort = sort_timer(arr)
    print("Fastest sort algorithm:", fastest_sort)
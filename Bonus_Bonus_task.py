import random
import timeit
import matplotlib.pyplot as plt

def quicksort_first_last(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        less = [num for num in lst[1:] if num <= pivot]
        greater = [num for num in lst[1:] if num > pivot]

    return quicksort_first_last(less) + [pivot] + quicksort_first_last(greater)

def quicksort_random(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = random.choice(lst)
        less = [num for num in lst if num <= pivot and num != pivot]
        greater = [num for num in lst if num > pivot and num != pivot]

    return quicksort_random(less) + [pivot] + quicksort_random(greater)

def quicksort_median(lst):
    if len(lst) < 2:
        return lst
    else:
        first = lst[0]
        second = lst[1]
        last = lst[-1]
        median = sorted([first, second, last])[1]
        
        pivot = median
        
        less = [num for num in lst if num < pivot]
        equal = [num for num in lst if num == pivot]
        greater = [num for num in lst if num > pivot]

    return quicksort_median(less) + equal + quicksort_median(greater)

# Generate a list of random integers
lst = [random.randint(0, 1000) for _ in range(1000)]

# Measure the execution time for each method
times_first_last = timeit.timeit(lambda: quicksort_first_last(lst), number=10)
times_random = timeit.timeit(lambda: quicksort_random(lst), number=10)
times_median = timeit.timeit(lambda: quicksort_median(lst), number=10)

# Create a plot
methods = ['First/Last Element', 'Random Element', 'Median of Three']
times = [times_first_last, times_random, times_median]

plt.bar(methods, times)
plt.xlabel('Method')
plt.ylabel('Execution Time (seconds)')
plt.title('Comparison of Quicksort Methods')
plt.show()

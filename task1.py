#Exercise(pivot choice):
# In the Quicksort algorithm, the choice of the pivot can affect the efficiency of the sorting process:
# First or Last Element: One simple approach is to select the first or last element of the array as the pivot. This strategy is easy to implement but can be inefficient for already sorted or nearly sorted arrays.
# Random Element: Choosing a random element from the array as the pivot helps to eliminate bias in the pivot selection. Randomized pivot selection can provide good average-case performance, but it may still suffer from poor performance in certain scenarios.

# Refactor the following code:

# return quicksort(less) + [pivot] + quicksort(greater) 
# instead of using the second element as pivot use a random element as pivot.
# Compare the performance effect with the quicksort version above.

def quicksort(lst):
    if len(lst) < 2:
        return lst  #[2]
    else:
        pivot = lst[1]
        less = [num for num in lst[:1] + lst[2:] if num <= pivot]
        greater = [num for num in lst[:1] + lst[2:] if num > pivot]
        print('##############')
        print(f"pivot: {pivot}")
        print(f"less: {less}")
        print(f"greater: {greater}")

    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([12,10,13,25,37]))

print("______________________________________________")

# Solution
import random

def quicksort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = random.choice(lst)
        less = [num for num in lst if num <= pivot and num != pivot]
        greater = [num for num in lst if num > pivot and num != pivot]
        print('##############')
        print(f"pivot: {pivot}")
        print(f"less: {less}")
        print(f"greater: {greater}")

    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([12, 10, 13, 25, 37]))

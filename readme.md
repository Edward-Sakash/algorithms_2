# Exercise(pivot choice):
In the Quicksort algorithm, the choice of the pivot can affect the efficiency of the sorting process:
First or Last Element: One simple approach is to select the first or last element of the array as the pivot. This strategy is easy to implement but can be inefficient for already sorted or nearly sorted arrays.
Random Element: Choosing a random element from the array as the pivot helps to eliminate bias in the pivot selection. Randomized pivot selection can provide good average-case performance, but it may still suffer from poor performance in certain scenarios.
1:01
Refactor the following code:
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
    
instead of using the second element as pivot use a random element as pivot.
Compare the performance effect with the quicksort version above.

# Bonus Exercise(pivot choice):
Median-of-Three: The median-of-three pivot selection strategy aims to mitigate the potential issues with the first or last element selection. It involves selecting the median value among the first, middle, and last elements of the array as the pivot. This approach helps in reducing the chances of extreme imbalanced partitions.
instead of using the second element as pivot use the median of three

# Bonus Bonus:
compare all three methods using timeit.
Which method works faster whan the others?
Make a plot

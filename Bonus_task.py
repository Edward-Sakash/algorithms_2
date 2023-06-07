"""Bonus Exercise(pivot choice):
Median-of-Three: The median-of-three pivot selection strategy aims to mitigate the potential issues with the first or last element selection. It involves selecting the median value among the first, middle, and last elements of the array as the pivot. This approach helps in reducing the chances of extreme imbalanced partitions.
instead of using the second element as pivot use the median of three"""

# Solution
def quicksort(lst):
    if len(lst) < 2:
        return lst
    else:
        # Find the median of lst[0], lst[1], and lst[-1]
        first = lst[0]
        second = lst[1]
        last = lst[-1]

        # Calculate the median using sorted function
        median = sorted([first, second, last])[1]
        
        pivot = median
        
        less = [num for num in lst if num < pivot]
        equal = [num for num in lst if num == pivot]
        greater = [num for num in lst if num > pivot]
        
        print('##############')
        print(f"pivot: {pivot}")
        print(f"less: {less}")
        print(f"equal: {equal}")
        print(f"greater: {greater}")

    return quicksort(less) + equal + quicksort(greater)

print(quicksort([12, 10, 13, 25, 37]))



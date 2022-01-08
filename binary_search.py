def binary_search(ls: iter, item):
    low = 0
    high = len(ls) - 1

    while low <= high:
        mid_ind = (low + high) // 2
        if ls[mid_ind] == item:
            return mid_ind

        elif ls[mid_ind] > item:
            high = mid_ind - 1
        elif ls[mid_ind] < item:
            low = mid_ind + 1
        else:
            return None

def binary_searching(ls, item):
    low = 0
    high = len(ls)-1
    while low <= high:
        mid_ind = (low + high)//2
        guess = ls[mid_ind]
        if guess == item:
            return mid_ind
        elif guess<item:
            low = mid_ind + 1
        elif guess>item:
            high = mid_ind - 1


print(binary_searching([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))

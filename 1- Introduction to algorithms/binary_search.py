def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == x:
            return mid
        elif guess > x:
            high = mid - 1
        else:
            low = mid + 1
    return None

#test array
my_list = [1, 3, 5, 7, 9, 20]
x = 5
#function call
result = binary_search(my_list, x)

if result != None:
    print("Sayi {}. indexte".format(result))
else:
    print("Sayi listede yok")

 

lst = [int(x) for x in input().split()]

# Nesting a compound conditional in a for loop

largest = 0

for num in lst:
    # test if num is even and greater than largest
    if((largest < num) and (num % 2 == 0)):
        largest = num

print("Largest even number in the list is: ", largest)

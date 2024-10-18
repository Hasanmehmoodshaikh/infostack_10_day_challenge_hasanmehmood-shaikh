def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

print("Test case 1")
print("input  - ",1234)
print("Output - ",sum_of_digits(1234))

print("\nTest case 2")
print("input - ",987)
print("output -",sum_of_digits(987))

n= int(input("\nEnter a positive integer - "))
print("sum of digit - ",sum_of_digits(n))
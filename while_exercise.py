odd_num=[1, 3, 5, 7, 9]
even_num=[2, 4, 6, 8, 10]

first_number = int(input("Please enter a number: \n"))

while first_number <= 10:
    if first_number in odd_num:
        print(f"{first_number} is odd number")
        break
    else:
        print(f"{first_number} is even number")
        break 
 
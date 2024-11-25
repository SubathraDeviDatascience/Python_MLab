def sum_of_square_series(number):
   if(number == 0):
     return 0
   else:
     return (number * number) + sum_of_square_series(number - 1)
num = int(input("Please Enter any Positive Number : "))
total = sum_of_square_series(num)
print("The Sum of Series upto {0} = {1}".format(num, total))
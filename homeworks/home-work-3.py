# from random import randint

# # 1. დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს "n" და ბეჭდავს 1-დან "n"-მდე რიცხვების ჯამს.

# n = eval(input(f'Please enter a number: '))
# num = 0
# for i in range(1, n + 1):
#     num += i

# print(num)


# # 2.დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს და შემდეგ იყენებს "while" ციკლს 
# # რომ რევესრულად დაბეჭდოს რიცხვები 0-მდე. მაგალითად თუ შეიყვანს 4, დაიბეჭდოს 4, 3, 2, 1

# n = int(input(f'Please enter a number: '))

# while n > 0:
#     print(n)
#     n -= 1


# # 3.დაწერეთ პითონის პროგრამა თამაშისთვის, რომელიც მუდმივად სთხოვს მომხმარებელს გამოიცნოს წინასწარ განსაზღვრული რიცხვი.
# #  როდესაც მომხმარებელი გამოიცნობს სწორ რიცხვს, დაასრულებს პროგრამა მუშაობას.

# num = randint(1, 100)
# i = 0

# print( f"Please guess a number between 1 and 100: ")

# while True:
#   i += 1
#   guess = int(input(f"Try N{i}. Your guess: "))

#   if guess == num:
#     print(f"Congrats...! It was {num}.")
#     break
#   elif guess > num:
#     print(f"Too great")
#   else:
#     print(f"Too less")
  
# print(f"Game Over!")

# # 4.დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მუდმივად რიცხვებს. შექმენით საწყისი ცვლადი total_sum = 0, შეამოწმეთ რიცხვი თუ დადებითია,
# #  მხოლოდ მაშინ დაუმატეთ total_sum ცვლადს. ეს პროცესი გაგრძელდეს იქამდე სანამ მომხმარებელი არ შეიყვანს 'sum' ტექსტს, 
# # რის შემდეგაც დაიბეჭდება შეყვანილი დადებითი რიცხვების ჯამი.


    
# total_sum = 0

# while True:
#     user_input = input(f"Enter a number (type 'sum' to end and calculate sum): ")

#     if user_input == "sum":
#         break

#     num = float(user_input)

#     if num > 0:
#             total_sum += num
#     else:
#         print(f"Invalid input.Please enter a number greater than 0 or 'sum'.")

# print(f"Total sum:", int(total_sum))




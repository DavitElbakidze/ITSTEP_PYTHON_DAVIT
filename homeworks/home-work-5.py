# 1.დაწერეთ პითონის პროგრამა, რომელიც დასაწყისში შექმნის ცარიელ სიას ([]), თუ მომხარებელი შეიყვანს სიმბოლო 'a'-ს, ნიშნავს რომ უნდა 
# დაამატოთ სიაში რიცხვი; თუ აკრიფა 'r', სიიდან უნა წაიშალოს რიცხვი; 'e'-ს შეტანისას პროგრამამ უნდა დაასრულოს მუშაობა. მიღებული შედეგი 
# დაბეჭდეთ კონსოლში.
# მომხარებელმა უნდა შეიყვანოს შემდეგი სტრუქტურით ბრძანება "{command} {number}" commands:

# a – append
# r – remove
# e – exit
# მხოლოდ გამოიყენეთ ეს ბრძანებები და მოახდინეთ სიაზე ზემოქმედება.

number_list = []

while True:
    user_input = input("Enter command (a, r, e): ")

    if not user_input:
        print("Please enter a valid command.")
        continue

    command = user_input[0]

    if command == 'a':
        number = int(input("Enter the number to append: "))
        number_list.append(number)
    elif command == 'r':
        number = int(input("Enter the number to remove: "))
        if number in number_list:
            number_list.remove(number)
        else:
            print(f"{number} not found in the list.")
    elif command == 'e':
        break
    else:
        print("Invalid command. Please enter 'a', 'r', or 'e'.")

print("Final List:", number_list)


# 2.დაწერეთ პითონის პროგრამა, რომელიც შექმნის სიას my_list = [43, '22', 12, 66, 210, ["hi"], და შეასრულებს შემდეგ ნაბიჯებს:
# a. დაბეჭდავს 210-ის ინდექსს;
# b. დაამატებს ბოლო ელემენტში ტექსტს "hello";
# c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს სიას;
# d. შექმენით ახალი სია my_llist_2, რომელსაც ექნება my_llist-ის მნიშვნელობა, გაასუფთავეთ my_llist_2-ის მნიშნველობა და დაბეჭდეთ ორივე სია.

my_list = [43, '22', 12, 66, 210, ["hi"]]

index_of_210 = my_list.index(210)
print("Index of 210:", index_of_210)

my_list[-1].append("hello")
print("List after adding 'hello':", my_list)

del my_list[2]
print("List after deleting element at index 2:", my_list)

my_list2 = my_list.copy()

my_list2.clear()
print("my_list:", my_list)
print("my_list2:", my_list2)

# 3.დაწერეთ პითნის პროგრამა, რომელიც მიიღებს ტელეფონის ნომერს და regex-ით შეამოწმებს შეყვანილი ნომერი იცავს თუ არა "(123) 456-789" ფორმატს, 
# თუ იცავს დააბრუნეთ შეყნვაილი ტელეფონის ნომერი, წინააღმდეგ შემთხვევაში გამოიტანეთ "Invalid format" ტექსტი.

import re

pattern = re.compile(r'^\(\d{3}\) \d{3}-\d{3}$')

user_input = input("Enter a phone number: ")

match = pattern.match(user_input)

if match:
    print("Valid phone number:", user_input)
else:
    print("Invalid phone number format")

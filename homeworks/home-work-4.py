# 1. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს სტრიქონის UTF-8 დაშიფრულ ვერსიას.
str = input('Please enter string: ')

encoded_string = str.encode('utf-8')

print(encoded_string)


# 2. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს. ჩამოაშორეთ ზედმეტი ინტერვალები. ყველა სიმბოლო გადაიყვანეთ პატარა ასოებში და 
# დაუმატეთ ქვესტრიქონი 'Python'. თუ შეყვანილ სტრიქონში არსებობს სიტყვა "python", ჩაანაცვლეთ "Python"-ით.
# მინიშნება: ზედმეტი ინტერვალების ჩამოსაშორებელი მეთოდია .strip()

str = input('Please enter string: ')
new_str =' '.join(str.split()).lower() + " Python"
if "python" in new_str:   
  new_str1 =   new_str.replace("python", "Python")
  print(new_str1)
else:
  print(new_str)





# 3.დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს ახალ სტრიქონს, რომელიც შედგება შეყვანილი სტრიქონის პირველი ნახევრისაგან.
str = input('Please enter string: ')

str_len = len(str)

new_str = str[: str_len // 2]

print(new_str)



# 4. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს. string მოდულის გამოყენებით დაწერეთ შემოწმება. სტრიქონი ვალიდურია მაშინ, როდესაც ის
#  შეიცავს ერთ ციფრს და არ არის დამატებითი სიმბოლოები ('!', '~', '#', '$' და ა.შ.)
import string

letters = string.ascii_lowercase + string.ascii_uppercase
digits = string.digits
chars = string.punctuation

digit = False
letter = False
char = False

str = input('Please enter a string: ')

for ch in str:
    if ch in letters:
        letter = True
    elif ch in digits:
        digit = True
    elif ch in chars:
        char = True

validation = digit and letter and not char

if validation:
    print("Nice! Valid string.")
else:
    print("Invalid string.")



# 5. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს, სტრიქონი გადაყავს ბაიტებში, ბეჭდავს მნიშვნელობას და 
# შემდეგ კი გადაყავს ბაიტებიდან სტრიქონში და ბეჭდავს სტრიქონს.


import base64

str = input('Please enter a string: ')

encoded_str = base64.b64encode(str.encode('utf-8'))

decoded_str = base64.b64decode(encoded_str).decode('utf-8')

print("Original String:", str)
print("Encoded Bytes:", encoded_str)
print("Decoded String:", decoded_str)
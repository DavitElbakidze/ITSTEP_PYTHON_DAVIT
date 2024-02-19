# 1.შექმენით გლობალური ცვლადი int_list = [10,20,30,40] და დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს
#  რიცხვს პარამეტრად და გლობალურ int_list სიაში ჩაამატებს პარამეტრად მიღებულ რიცხვს.

int_list = [10, 20, 30, 40]

def add_int_list(number):
    global int_list
    int_list.append(number)

add_int_list(60)

print(f"updated int_list: {int_list}")

# 2.დაწერეთ პითნის ფუნქცია რომელიც პარამეტრად იღებს რიცხვების სიას (ლისტს) და აბრუნებს რიცხვების ჯამს.
#  პარამეტრად უნდა მიიღოს შემდეგი სია [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10].

def calculate_sum(num_list):
    return sum(num_list)

numbers = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
result = calculate_sum(numbers)

print(f"The sum of the numbers is: {result}")


# 3.შექმენით გლობალური ცვლადი gl_str = "Global" და დაწერეთ პითონის ფუნქცია რომელიც ქმნის ლოკალურ ცვლადს იგივე
#  სახელით რაც გლობალურ ცვლადს აქვს (gl_str) და აბრუნებს ლოკალური ცვლადის მნიშვნელობას

gl_str = "Global"  

def local_variable():
    gl_str = "Local"
    return gl_str

local_result = local_variable()
print(f"Local variable: {local_result}")

# 4.რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს ერთ პარამეტრს number და დააბრუნებს ციფრების ჯამს
#  (მაგალითად თუ ფუნქციამ მიიღო რიცხვი 12345, უნდა დააბრუნოს 15. რადგან 1+2+3+4+5 უდრის 15-ს).

def recursive_sum(number):
    if number == 1:
        return 1
    else:
        return number + recursive_sum(number - 1)

result = recursive_sum(5)
print(result)

# 5.რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრიქონს და დააბრუნებს მის შებრუნებულ
#  (revers) სტრიქონს (მაგალითად input: Hello   Output: olleH)

def reverse_string(input_str):
    if len(input_str) <= 1:
        return input_str
    else:
        return reverse_string(input_str[1:]) + input_str[0]

result = reverse_string("string")
print(f"The reversed string is: {result}")


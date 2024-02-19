# 1.დაწერეთ პითნის ფუნქცია, რომელიც იღებს პარამეტრად ერთი დაიგივე ზომის სიას (list) და zip ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები.
# params: [1, 2, 3], ['a', 'b', 'c']  
# outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]

def zip_lists(list1, list2):
    zipped_list = zip(list1, list2)
    
    formatted_list = [f"({x}, '{y}')" for x, y in zipped_list]
    
    return formatted_list

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

result = zip_lists(list1, list2)
print(result)

# 2.დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს. ფუნქციაში გაითვალისწინეთ
#  გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).
# ფუქნციის დასაწერად გამოიყენეთ lambda და functools-ის reduce მეთოდი.

# params:[1, 2, 3, 4, 5] 
# output: 120

from functools import reduce

def multiply_elements(numbers):
    try:
        if not numbers:
            raise ValueError("Input list is empty")

        if not all(isinstance(num, (int, float)) for num in numbers):
            raise TypeError("All elements in the list must be numeric")

        result = reduce(lambda x, y: x * y, numbers)

        return result
    except (ValueError, TypeError) as e:
        return f"Error: {str(e)}"

number_list = [1, 2, 3, 4, 5]
result = multiply_elements(number_list)
print(result)


# 3.დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.
# params: [1, 2, 3, 4, 5, 6, 7]
# outputs: [1, 3, 5, 7]

numbers = [1, 2, 3, 4, 5, 6, 7, 9, 10]

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print(odd_numbers)


# 4.დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending). დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც
#  მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით. გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError), 
# თუ სხვა გამონაკლისიც აღმოჩნდა ისიც გაითვალისწინეთ.
# მინიშნება: გადაავლეთ თვალი string მეთოდებს, მონახეთ ისეთი მეთოდი, რომელიც აბრუნებს სიტყვას, რომელიც მთავრდება რაღაც სიმბოლოებით...

# params: ['hello', 'world', 'coding', 'nod'], 'ing'  
# outputs: ['coding']

def filter_by_suffix(string_list, suffix):
    try:
        if not isinstance(suffix, str):
            raise TypeError("Suffix must be a string")

        filtered_list = list(filter(lambda x: x.endswith(suffix), string_list))

        return filtered_list
    except TypeError as e:
        return f"Error: {str(e)}"

string_list = ['hello', 'world', 'coding', 'noding']
suffix = 'ing'

result = filter_by_suffix(string_list, suffix)
print(result)

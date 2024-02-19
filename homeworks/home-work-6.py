# 1.დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას.

def fibanacci(n):
  a, b = 0, 1
  
  for _ in range(n + 1):
    print(a, end=' ')
    
    a, b = b, a+b


fibanacci(10)



# 2.დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად ორ სტრიქონს და შეამოწმებს არის თუ არა სტრიქონები ანაგრამები.
#  (ანაგრამი არის სიტყვა ან შესიტყვება, რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების ასოების გადაადგილებით). მაგ.: race და care ანაგრამებია.

# def are_anagrams(str1, str2):
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()

#     is_anagrams = sorted(str1) == sorted(str2)
#     if is_anagrams:
#         return print(f"{str1} and {str2} are anagrams")
#     else:
#         return print(f"{str1} and {str2} are not anagrams")

# 3.დაწერეთ პითონის ფუნქცია რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს.

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# print (factorial(4))


# 4.დაწერეთ პითნის ფუნქცია რომელიც მიიღებს ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს. ფუნქციამ უნდა მოძებნოს სტრიქონში
#  რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს მისი რაოდენობა.

# def count_symbol(str, sym):
#     count = 0
#     for i in str:
#         if sym == i:
#          count +=1
#     return count


      
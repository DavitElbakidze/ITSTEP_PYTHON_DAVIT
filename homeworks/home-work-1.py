#  1. დაწერეთ პროგრამა რომელიც input მეთოდის საშუალებით მიიღებს 2 რიცხვს და დააბრუნებს ამ რიცხვებს
#  შორის შესრულებული არითმეტიკული ოპერაციების შედეგებს (მიმატება, გამოკლება, გამრავლება, გაყოფა, ახარისხება).
numb_1 = eval(input('Please  enter first number: '))
numb_2 = eval(input('Please  enter second number: '))
print(f"The sum is: {numb_1} + {numb_2} = {numb_1 + numb_2}")
print(f"The sub is: {numb_1} - {numb_2} = {numb_1 - numb_2}")
print(f"The mult is: {numb_1} * {numb_2} = {numb_1 * numb_2}")
print(f"The div  is: {numb_1} / {numb_2} = {numb_1 / numb_2}")
print(f"The exp is: {numb_1} ** {numb_2} = {numb_1 ** numb_2}")




# 2. დაწერეთ პროგრამა რომბის ფართობის გამოსათვლელად. მომხმარებელს კლავიატურის გამოყენებით შეაქვს ორი დიაგონალის სიგრძე.

diagonal_1 = eval(input('Please enter first number: '))
diagonal_2 = eval(input('Please enter second number: '))

print(f"Area of the rhombus is: ({diagonal_1} * {diagonal_2}) / 2 = {diagonal_1 * diagonal_2 / 2}")



# 3. მომხმარებელის შეაქვს მეტრების რაოდენობა. დაბეჭდეთ შესაბამისი მნიშვნელობა სანტიმეტრებში, დეციმეტრებში, მილიმეტრებში, მილში.
numb_1 = eval(input('Please enter number: '))

print(f"There are {numb_1 * 100} centimeters in {numb_1} meter ")
print(f"There are {numb_1 * 10} decimeter in {numb_1} meter ")
print(f"There are {numb_1 * 0.00062137} mile in {numb_1} meter ")
print(f"There are {numb_1 * 1000} millimeter in {numb_1} meter ")



# 4. დაწერეთ პროგრამა, რომელიც ითვლის სამკუთხედის ფართობს. მომხმარებელს კონსოლიდან შეყავს სამკუთხედის სიმაღლისა და ფუძის მნიშვნელობა.

base = eval(input('Please enter the base of the triangle: '))
height = eval(input('Please enter the height of the triangle: '))

print(f"Area of the triangle is: ({base} * {height}) / 2 = {base * height / 2}")
# დაწერეთ პითნის პროგრამა, რომელიც გააგზავნის მოთხოვნას requests-მოდულის გამოყენებით "https://fakestoreapi.com/products" მისამართზე, შეამოწმებს
#  სტატუს და გადაიყვანს მიღებულ სიას, პითონის ლისტად და შეასრულეთ შემდეგი მოქმედებები:


# ა)შექმენით პროდუქტის ფასების სია და გამოიტანეთ როგორც მაქსიმალური ასევე მინიმალური და სასშუალო ფასები
# ბ) შექმენით კატეგორიების სია (დუბლიკაციების გარეშე) და დაასორტირეთ
# გ) შექმენით სია რომელშიც გექნებად პროდუქტის აღწერა (title) და id. დაასორტირეთ შედეგი title-ის მიხედვით
# დ) შემქენით რეიტინგების სია რომელიც იქნება დასორტირებული ("rate"-ის მიხედვით) ზრდადობით

# https://jsonformatter.curiousconcept.com/

import requests

def fetch_product_data(url):
    
    try:

      response = requests.get(url)

      if response.status_code == 200:
        return response.json()
    except requests.exceptions.HTTPError as err:
      print("Http error: {err}")
    except requests.exceptions.ConnectionError as con_err:
      print(f"Connection error: {con_err}")
    except Exception as err:
      print(f"Somethin g wrong error: {err}")

def create_price_list(products):
    prices = [product['price'] for product in products]
    max_price = max(prices)
    min_price = min(prices)
    average_price = sum(prices) / len(prices)

    return {'max_price': max_price, 'min_price': min_price, 'average_price': average_price}

def create_category_list(products):
    categories = set(product['category'] for product in products)
    sorted_categories = sorted(categories)
    
    return sorted_categories

def create_title_list(products):
    title_list = [(product['id'], product['title']) for product in products]
    sorted_title_list = sorted(title_list, key=lambda x: x[1])
    
    return [{'product_id': product_id, 'title': title} for product_id, title in sorted_title_list]

def create_rating_list(products):
    rating_list = [(product['id'], product['rating']['rate']) for product in products]
    sorted_rating_list = sorted(rating_list, key=lambda x: x[1])
    
    return [{'product_id': product_id, 'rate': rate} for product_id, rate in sorted_rating_list]

url = "https://fakestoreapi.com/products"

products = fetch_product_data(url)

if products:
    price_list = create_price_list(products)
    print("Price List:", price_list)

    category_list = create_category_list(products)
    print("Category List:", category_list)

    title_list = create_title_list(products)
    print("Title List:", title_list)

    rating_list = create_rating_list(products)
    print("Rating List:", rating_list)


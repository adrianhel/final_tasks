purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]


def total_revenue(purchases: list[dict]) -> float:
    total_price = 0
    for purchase in purchases:
        total_price += purchase["price"] * purchase["quantity"]
    return total_price


def items_by_category(purchases: list[dict]) -> dict:
    items_by_category = {}
    for purchase in purchases:
        if purchase["category"] not in items_by_category:
            items_by_category[purchase["category"]] = []
        items_by_category[purchase["category"]].append(purchase["item"])
    return items_by_category


def expensive_purchases(purchases: list[dict], min_price: float) -> list[dict]:
    expensive_purchases = []
    for purchase in purchases:
        if purchase["price"] > min_price:
            expensive_purchases.append(purchase)
    return expensive_purchases


def average_price_by_category(purchases: list[dict]) -> dict:
    price_by_category = {}
    for purchase in purchases:
        if purchase["category"] not in price_by_category:
            price_by_category[purchase["category"]] = []
        price_by_category[purchase["category"]].append(purchase["price"])

    average_price_by_category = {}
    for category, prices in price_by_category.items():
        average_price_by_category[category] = sum(prices) / len(prices)
    return average_price_by_category


def most_frequent_category(purchases: list[dict]) -> str:
    category_count = {}
    for purchase in purchases:
        if purchase["category"] not in category_count:
            category_count[purchase["category"]] = 0
        category_count[purchase["category"]] += 1
    return max(category_count, key=category_count.get)


print("Общая выручка:", total_revenue(purchases))
print("Товары по категориям:", items_by_category(purchases))
print("Покупки дороже 1.0:", expensive_purchases(purchases, 1.0))
print("Средняя цена по категориям:", average_price_by_category(purchases))
print("Категория с наибольшим количеством проданных товаров:", most_frequent_category(purchases))
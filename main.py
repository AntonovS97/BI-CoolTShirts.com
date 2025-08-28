import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

cart_plus_visits = visits.merge(cart, how = 'left')
print(len(cart_plus_visits))
no_cart = cart_plus_visits['cart_time'].isnull().sum()
print(no_cart)
percent_no_cart = no_cart / len(cart_plus_visits) * 100
print(percent_no_cart)

cart_plus_checkout = cart.merge(checkout, how = 'left')
print(len(cart_plus_checkout))
no_checkout = cart_plus_checkout['checkout_time'].isnull().sum()
print(no_checkout)
percent_no_checkout = no_checkout/ len(cart_plus_checkout) * 100
print(percent_no_checkout)

checkout_plus_purchase = checkout.merge(purchase, how = 'left')
print(len(checkout_plus_purchase))
no_purchase = checkout_plus_purchase['purchase_time'].isnull().sum()
print(no_purchase)
percent_no_purchase = no_purchase/ len(checkout_plus_purchase) * 100
print(percent_no_purchase)


print(f"Did not add to cart: {percent_no_cart:.2f}%")
print(f"Did not proceed to checkout: {percent_no_checkout:.2f}%")
print(f"Did nit purchase: {percent_no_purchase:.2f}%")

all_data = visits.merge(cart, how = 'left').merge(checkout, how = 'left').merge(purchase, how = 'left')

all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
print(all_data)
print(all_data.time_to_purchase.mean())
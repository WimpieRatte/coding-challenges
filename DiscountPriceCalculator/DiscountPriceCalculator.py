price = float(input("Enter the price of your item: "))
discount_rate = float(input("Enter the discount rate: "))
discount = price * discount_rate / 100
discounted_price = price - discount
print(f"Price Before Discount: {price}")
print(f"Discount Rate: {discount_rate}%")
print(f"Disount: {discount}")
print(f"Price after discount: {discounted_price}")

# Function to calculate discount
def calculate_discount(price, discount_percent):
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied
        return price


# Ask user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(price, discount_percent)

# Print result
if discount_percent >= 20:
    print(f"The final price after {discount_percent}% discount is: {final_price}")
else:
    print(f"No discount applied. The original price is: {final_price}")


# Define the function to calculate the final price
def calculate_discount(price, discount_percent):
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        # Calculate and return the discounted price
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        # Return the original price if discount is less than 20%
        return price

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Use the function to calculate the final price
final_price = calculate_discount(original_price, discount_percent)

# Print the result
if discount_percent >= 20:
    print(f"The final price after applying the discount is: {final_price}")
else:
    print(f"No discount applied. The original price is: {final_price}")

class Market:
    def __init__(self, barcode, name, manufacturer, price, quantity):
        # Initialize the product attributes
        self.barcode = barcode
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.quantity = quantity

    def sale(self, quantity):
        """Sell a certain quantity of the product"""
        if quantity <= self.quantity:
            self.quantity -= quantity
            print(f"Remaining: {self.quantity}")
        else:
            print("Not enough quantity in stock!")

    def discount(self):
        """Apply discount based on the price range"""
        if 30 <= self.price <= 50:
            self.price *= 0.95  # 5% discount
        elif 10 <= self.price < 30:
            self.price *= 0.93  # 7% discount
        else:
            pass  # No discount
        self.price = round(self.price, 2)

    def show(self):
        """Display product information"""
        print(f"Barcode: {self.barcode}")
        print(f"Name: {self.name}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
        print("-----------------------------")


def search_by_barcode(product_list, barcode):
    """Find a product by its barcode"""
    found = False
    for product in product_list:
        if product.barcode == barcode:
            product.show()
            found = True
            break

    if not found:
        print("Wrong barcode!!!")
        print("Available barcodes:")
        for p in product_list:
            print(p.barcode, end=" | ")
        print()


def search_by_manufacturer(product_list, manufacturer):
    """Find all products from a given manufacturer cheaper than or equal to the average price"""
    manufacturer_list = [
        p for p in product_list if p.manufacturer.lower() == manufacturer.lower()]

    if not manufacturer_list:
        print("There are no products from this manufacturer.")
        return []

    # Calculate average price for that manufacturer
    avg_price = sum(p.price for p in manufacturer_list) / \
        len(manufacturer_list)

    # Filter all products cheaper than or equal to average price
    result_list = [p for p in manufacturer_list if p.price <= avg_price]

    print(f"Average price for {manufacturer}: {avg_price:.2f}")
    print("Products cheaper or equal to the average:")
    for p in result_list:
        p.show()

    return result_list


def sort_by_quantity(product_list):
    """Sort and display all products by ascending quantity"""
    sorted_list = sorted(product_list, key=lambda x: x.quantity)
    print("Products sorted by ascending quantity:")
    for p in sorted_list:
        p.show()
    return sorted_list


def delete_by_name(product_list, name):
    """Delete all products with the given name and quantity <= 3"""
    original_len = len(product_list)
    product_list[:] = [p for p in product_list if not (
        p.name == name and p.quantity <= 3)]

    if len(product_list) < original_len:
        print(f"Products named '{name}' with quantity <= 3 were deleted.")
        print("The number of products now is:", len(product_list))
    else:
        print("No products were deleted.")


# --- Main program with error handling ---
try:
    n = int(input("How many products? "))
    product_list = []

    # Input product data
    for i in range(n):
        print(f"\nEnter data for product {i + 1}:")
        barcode = int(input("Barcode: "))
        name = input("Name: ")
        manufacturer = input("Manufacturer: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))

        # Create a Market object and add it to the list
        product = Market(barcode, name, manufacturer, price, quantity)
        product_list.append(product)

    print("\n--- Applying discounts ---")
    for p in product_list:
        p.discount()

    print("\n--- Search by barcode ---")
    search_by_barcode(product_list, int(input("Enter the barcode: ")))

    print("\n--- Search by manufacturer ---")
    search_by_manufacturer(product_list, input("Enter the manufacturer: "))

    print("\n--- Sort by quantity ---")
    sort_by_quantity(product_list)

    print("\n--- Delete by name ---")
    delete_by_name(product_list, input("Enter the product name: "))

except Exception as e:
    print("Unexpected error occurred:", e)

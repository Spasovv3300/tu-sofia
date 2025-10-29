# Class representing a clothing item in a shop
class ClothesShop():
    # Constructor that initializes object attributes
    def __init__(self, id, type, brand, price, quantity):
        self.id = id              # Unique identifier for the clothing item
        self.type = type          # Type of clothing (e.g., "Jacket", "Pants")
        self.brand = brand        # Brand name
        self.price = price        # Price of the item
        self.quantity = quantity  # Quantity available in stock

    # Method that prints detailed information about the item
    def clothe_info(self):
        print("Id:", self.id)
        print("Type:", self.type)
        print("Brand:", self.brand)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    # Method to change the price of the item
    def change_price(self):
        try:
            self.price = float(input("Enter the new price: "))
        except ValueError:
            print("Invalid input! Price must be a number.")

    # Method to change the quantity of the item
    def change_qty(self):
        try:
            self.quantity = int(input("Enter the new quantity: "))
        except ValueError:
            print("Invalid input! Quantity must be an integer.")

    # Destructor - runs when the object is deleted
    def __del__(self):
        print("Destructor called for", self.type)


# Function to search for an item by its ID and print its info
def search_by_id(clothes_list, id):
    found = False
    for k in clothes_list:
        if id == k.id:
            k.clothe_info()
            found = True
            break
    if not found:
        print("No item found with this ID.")


# Function to search for items by brand name
def search_by_brand(clothes_list, brand):
    listing = []  # Will hold the types of clothes from the given brand
    for k in clothes_list:
        if brand.title() == k.brand:
            listing.append(k.type)

    if listing:
        print("Items from brand", brand + ":")
        for j in listing:
            print("-", j)
    else:
        print("There are no items from this brand.")


# Function to sell an item by ID
def sell_clothe_by_id(clothes_list, id, num):
    isFound = False  # Flag to track if the item was found
    for item in clothes_list:
        if id == item.id:
            isFound = True
            if item.quantity >= num:
                print("Successful sale!")
                item.quantity -= num
                print("Remaining quantity:", item.quantity)
            else:
                print("Not enough quantity available.")
    if not isFound:
        print("Product with this ID was not found.")


# --- Create objects from the ClothesShop class ---
item1 = ClothesShop(1, "Jacket", "La Coste", 499.99, 7)
item2 = ClothesShop(2, "Pants", "Diesel", 349.99, 10)
item3 = ClothesShop(3, "T-Shirt", "La Coste", 179.99, 15)

# List of all items available in the shop
clothes_list = [item1, item2, item3]

# --- Main program with try/except for safe user input ---
try:
    id_search = int(input("Enter the ID to search: "))
    search_by_id(clothes_list, id_search)

    brand_search = input("Enter the brand name: ")
    search_by_brand(clothes_list, brand_search)

    id_sell = int(input("Enter the ID of the item to sell: "))
    qty_sell = int(input("Enter the quantity to sell: "))
    sell_clothe_by_id(clothes_list, id_sell, qty_sell)

except ValueError:
    print("Invalid input! Please enter numbers where required.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

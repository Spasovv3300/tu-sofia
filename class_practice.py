class ClothesShop():
    def __init__(self, id, type, brand, price, quantity):
        self.id = id
        self.type = type
        self.brand = brand
        self.price = price
        self.quantity = quantity

    def clothe_info(self):
        print("Id:", self.id)
        print("Type:", self.type)
        print("Brand:", self.brand)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        # print(vars(self))
        # for attr, value in vars(self).items():
        #   print(f"{attr}:{value}")
        # print(self.__dict__())
        # for attr, value in self.__dict__.items():
        #   print(f"{attr}:{value}")

    def change_price(self):
        self.price = float(input("Enter the new price:"))

    def change_qty(self):
        self.quantity = int(input("Enter the new quantity:"))

    def __del__(self):
        print("Destructor")


def search_by_id(clothes_list, id):
    for k in clothes_list:
        if id == k.id:
            k.clothe_info()


def search_by_brand(clothes_list, brand):
    listing = []
    for k in clothes_list:
        if brand.title() == k.brand:
            listing.append(k.type)

    if listing:
        for j in listing:
            print(j)
    else:
        print("There are no items from this brand")


def sell_clothe_by_id(clothes_list, id, num):
    isFound = False
    for item in clothes_list:
        if id == item.id:
            isFound = True
            if item.quantity >= num:
                print("Successful sale")
                item.quantity -= num
                print("Remaining quantity:", item.quantity)
            else:
                print("Not enough quantity")
    if not isFound:
        print("The product is not found")


item1 = ClothesShop(1, "Jacket", "La Coste", 499.99, 7)
item2 = ClothesShop(2, "Pants", "Diesel", 349.99, 10)
item3 = ClothesShop(3, "T-Shirt", "La Coste", 179.99, 15)

clothes_list = [item1, item2, item3]

search_by_id(clothes_list, int(input("Enter the id:")))
search_by_brand(clothes_list, input("Enter the brand name:"))
sell_clothe_by_id(clothes_list, int(input("Enter the id:")),
                  int(input("Enter the amount:")))

class Product:
    def __init__(self, id, name, price, quantity, category):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def to_dict(self):
      return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "category": self.category
      }

# In-memory data store (replace with a database for production)
inventory = [
    Product(1, "Croissant", 3.50, 50, "Pastry"),
    Product(2, "Chocolate Cake", 25.00, 10, "Cake"),
    Product(3, "Sourdough Bread", 8.00, 20, "Bread"),
]

def get_products():
    return [product.to_dict() for product in inventory]


def get_product_by_id(id):
    for product in inventory:
        if product.id == id:
            return product.to_dict()
    return None


def add_product(name, price, quantity, category):
  new_id = max([p.id for p in inventory] or [0]) + 1
  new_product = Product(new_id, name, price, quantity, category)
  inventory.append(new_product)
  return new_product.to_dict()

def update_product(id, name=None, price=None, quantity=None, category=None):
  for product in inventory:
    if product.id == id:
      if name:
        product.name = name
      if price is not None:
        product.price = price
      if quantity is not None:
        product.quantity = quantity
      if category:
        product.category = category
      return product.to_dict()
  return None


def delete_product(id):
    global inventory
    inventory = [product for product in inventory if product.id != id]
    return True

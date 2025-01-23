import graphene

class Product(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    price = graphene.Float()
    quantity = graphene.Int()
    category = graphene.String()

class Query(graphene.ObjectType):
    products = graphene.List(Product)
    product = graphene.Field(Product, id=graphene.ID(required=True))

    def resolve_products(root, info):
        return products_data

    def resolve_product(root, info, id):
        for product in products_data:
            if product['id'] == id:
                return product
        return None

class CreateProduct(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        price = graphene.Float(required=True)
        quantity = graphene.Int(required=True)
        category = graphene.String(required=True)

    product = graphene.Field(Product)

    def mutate(root, info, name, price, quantity, category):
        new_id = str(len(products_data) + 1)
        product = {'id': new_id, 'name': name, 'price': price, 'quantity': quantity, 'category': category}
        products_data.append(product)
        return CreateProduct(product=product)

class UpdateProduct(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        price = graphene.Float()
        quantity = graphene.Int()
        category = graphene.String()

    product = graphene.Field(Product)

    def mutate(root, info, id, name=None, price=None, quantity=None, category=None):
        for product in products_data:
            if product['id'] == id:
                if name:
                    product['name'] = name
                if price:
                    product['price'] = price
                if quantity:
                    product['quantity'] = quantity
                if category:
                    product['category'] = category
                return UpdateProduct(product=product)
        return None

class DeleteProduct(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    def mutate(root, info, id):
        global products_data
        products_data = [product for product in products_data if product['id'] != id]
        return DeleteProduct(ok=True)


class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

# Dummy data for the bakery inventory
products_data = [
    {'id': '1', 'name': 'Chocolate Cake', 'price': 25.0, 'quantity': 10, 'category': 'Cakes'},
    {'id': '2', 'name': 'Croissant', 'price': 3.5, 'quantity': 50, 'category': 'Pastries'},
    {'id': '3', 'name': 'Baguette', 'price': 4.0, 'quantity': 30, 'category': 'Bread'},
]
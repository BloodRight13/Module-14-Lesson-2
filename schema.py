import graphene
from model import get_products, get_product_by_id, add_product, update_product, delete_product

class Product(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    price = graphene.Float()
    quantity = graphene.Int()
    category = graphene.String()

class Query(graphene.ObjectType):
    products = graphene.List(Product)
    product = graphene.Field(Product, id=graphene.Int(required=True))

    def resolve_products(self, info):
        return get_products()

    def resolve_product(self, info, id):
        return get_product_by_id(id)

class AddProduct(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        price = graphene.Float(required=True)
        quantity = graphene.Int(required=True)
        category = graphene.String(required=True)

    product = graphene.Field(Product)

    def mutate(self, info, name, price, quantity, category):
      product = add_product(name, price, quantity, category)
      return AddProduct(product=product)


class UpdateProduct(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        price = graphene.Float()
        quantity = graphene.Int()
        category = graphene.String()

    product = graphene.Field(Product)

    def mutate(self, info, id, name=None, price=None, quantity=None, category=None):
      product = update_product(id, name, price, quantity, category)
      return UpdateProduct(product=product)


class DeleteProduct(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        result = delete_product(id)
        return DeleteProduct(ok=result)

class Mutation(graphene.ObjectType):
    add_product = AddProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

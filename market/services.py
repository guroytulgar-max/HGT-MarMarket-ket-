from .models import Product

class MarketService:
    def __init__(self):
        self.products = []

    def add_product(self, product_id, name, price, stock, category):
        product = Product(product_id, name, price, stock, category)
        self.products.append(product)
        return product

    def list_products(self):
        return [p.to_dict() for p in self.products]
    
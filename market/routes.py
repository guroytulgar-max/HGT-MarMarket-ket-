from .services import MarketService

market = MarketService()

def api_add_product(id, name, price, stock, category):
    return market.add_product(id, name, price, stock, category)

def api_list_products():
    return market.list_products()
    
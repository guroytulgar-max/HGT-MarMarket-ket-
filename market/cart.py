from .routes import market

class Cart:
    def __init__(self):
        self.items = []

    def add(self, product_id, quantity=1):
        for p in market.products:
            if p.product_id == product_id:
                self.items.append({
                    "id": p.product_id,
                    "name": p.name,
                    "price": p.price,
                    "quantity": quantity
                })
                return f"{p.name} sepete eklendi."
        return "Ürün bulunamadı."

    def remove(self, product_id):
        self.items = [i for i in self.items if i["id"] != product_id]
        return "Ürün sepetten çıkarıldı."

    def show(self):
        return self.items

    def total(self):
        return sum(i["price"] * i["quantity"] for i in self.items)
    
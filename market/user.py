class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.cart = []
        self.orders = []

    def to_dict(self):
        return {
            "id": self.user_id,
            "name": self.name,
            "cart": self.cart,
            "orders": self.orders
        }
    
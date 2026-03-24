from sensec import Sensec
from market.routes import (
    api_add_product, api_list_products, api_update_product,
    api_list_by_category, api_search
)
from market.cart import Cart
from market.user_service import UserService

sensec = Sensec()
cart = Cart()
users = UserService()

def create_user():
    uid = int(input("Kullanıcı ID: "))
    name = input("İsim: ")
    print(users.create_user(uid, name).to_dict())

def login():
    uid = int(input("Kullanıcı ID: "))
    print(users.login(uid))

def logout():
    print(users.logout())

def whoami():
    u = users.get_current_user()
    print(u.to_dict() if u else "Giriş yapılmamış.")

def test_market():
    api_add_product(1, "Elma", 10, 100, "Meyve")
    api_add_product(2, "Süt", 25, 50, "İçecek")
    api_add_product(3, "Ekmek", 8, 200, "Fırın")
    print(api_list_products())

sensec.add_option("1", "Market Test", test_market)
sensec.add_option("2", "Kullanıcı Oluştur", create_user)
sensec.add_option("3", "Giriş Yap", login)
sensec.add_option("4", "Çıkış Yap", logout)
sensec.add_option("5", "Aktif Kullanıcı", whoami)

while True:
    sensec.show()
    secim = input("Seçim: ")
    sensec.run(secim)
    
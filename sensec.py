class Sensec:
    def __init__(self):
        self.options = {}

    def add_option(self, key, description, function):
        self.options[key] = {
            "description": description,
            "function": function
        }

    def show(self):
        print("\n=== HGT SENSEC MENU ===")
        for key, data in self.options.items():
            print(f"{key} - {data['description']}")

    def run(self, key):
        if key in self.options:
            return self.options[key]["function"]()
        else:
            print("Geçersiz seçenek.")
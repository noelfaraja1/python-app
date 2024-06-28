class phone:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phone_number):
        print(f"{self.brand} phone is calling {phone_number}")

    def __str__(self) -> str:
        return  f"Brand = {self.brand} Price = {self.price}"

iphone = phone("iPhone 7+", 300)
samsung = phone("samsung s22+", 150)

print(iphone.brand)
print(iphone.price)
iphone.call(35383)

print(samsung.brand)
print(samsung.price)
samsung.call(8363859)

print(iphone)
print(samsung)
from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79991234567"),
    Smartphone("Samsung", "Galaxy S24", "+79887654321"),
    Smartphone("Xiaomi", "Mi 14", "+79551112233"),
    Smartphone("Google", "Pixel 8", "+79001112233"),
    Smartphone("OnePlus", "12", "+79223334455"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")

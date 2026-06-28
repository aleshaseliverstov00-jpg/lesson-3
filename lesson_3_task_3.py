from address import Address
from mailing import Mailing

# Создаём адреса
to_addr = Address("123456", "Москва", "Тверская", "15", "7")
from_addr = Address("654321", "Санкт-Петербург", "Невский", "22", "12")

# Создаём отправление
mailing = Mailing(to_addr, from_addr, 350.0, "TRK123456789")

# Вывод в требуемом формате
print(
    f"Отправление {mailing.track} из "
    f"{mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - "
    f"{mailing.from_address.apartment} в "
    f"{mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)
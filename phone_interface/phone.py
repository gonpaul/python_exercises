class Phone:
    def __init__(
        self,
        brand: str,
        model: str,
        price: float,
        color: str,
        storage_gb: int,
        is_in_stock: bool
    ):
        self.brand: str = brand
        self.model: str = model
        self.price: float = price
        self.color: str = color
        self.storage_gb: int = storage_gb
        self.is_in_stock: bool = is_in_stock

    def get_full_name(self) -> str:
        """
        Возвращает строку в формате "Бренд Модель"
        """
        return f"{self.brand} {self.model}"

    def apply_discount(self, discount_percent: float) -> None:
        """
        Уменьшает цену телефона на заданный процент.
        """
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("discount_percent должен быть в интервале [0, 100]")
        self.price -= self.price * (discount_percent / 100)

    def check_availability(self) -> str:
        """
        Возвращает сообщение о наличии телефона.
        """
        return "В наличии" if self.is_in_stock else "Нет в наличии"
    def __str__(self) -> str:
        """
        Возвращает полное описание устройства в формате "Бренд Модель Объём_Памяти Цвет Цена В_Наличии"
        """
        stock_message = "В наличии" if self.is_in_stock else "Нет в наличии"
        return f"{self.brand} {self.model} {self.storage_gb}гб {self.color} {self.price}(руб) {stock_message}"

        
def test_phone_one():
    new_phone = Phone("Samsung", "S30", 12000, "Gray", 64, True)
    assert new_phone.get_full_name() == "Samsung S30"
    assert new_phone.check_availability() == "В наличии"
    new_phone.apply_discount(10)
    assert new_phone.price == 10800
    print(new_phone)

def test_phone_two():
    phone = Phone("Apple", "iPhone 14", 90000, "Black", 128, False)
    assert phone.get_full_name() == "Apple iPhone 14"
    assert phone.check_availability() == "Нет в наличии"
    phone.apply_discount(20)
    assert phone.price == 72000
    print(phone)

def test_phone_three():
    phone = Phone("Xiaomi", "Redmi Note 11", 17000, "Blue", 256, True)
    assert phone.get_full_name() == "Xiaomi Redmi Note 11"
    assert phone.check_availability() == "В наличии"
    phone.apply_discount(0)  # No discount
    assert phone.price == 17000
    print(phone)

test_phone_one()
test_phone_two()
test_phone_three()

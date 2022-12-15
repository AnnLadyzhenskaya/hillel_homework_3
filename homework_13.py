class Human:

    def __init__(self, name: str, surname: str, age: int, phone: str, address: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

        self.__private_info = "secure"
        self._protected_info = "secure"

    def get_info(self):
        return {key: value for key, value in vars(self).items() if not (key.startswith("__") or key.startswith("_"))}

    def call(self, phone_number: str):
        print(f"{self.phone} вызывает абонента {phone_number}")


h1 = Human("Ihor", "Petrenko", 25, "380975634562", "Address 1")
h2 = Human("Petr", "Sergeenko", 36, "380507652345", "Address 2")
h3 = Human("Dmitry", "Antonenko", 42, "380999879763", "Address 3")

print(f"Human 1: {h1.get_info()}")
print(f"Human 2: {h2.get_info()}")
print(f"Human 3: {h3.get_info()}")

print("\nIhor calls Petr:")
h1.call(h2.phone)


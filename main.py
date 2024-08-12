import collections

# Задание 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_list(num):
    first_factorial = factorial(num)
    return [factorial(i) for i in range(first_factorial, 0, -1)]

# Задание 2
pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        },
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        },
    },
}

def create():
    last = collections.deque(pets, maxlen=1)[0]
    new_id = last + 1
    name = input("Введите имя питомца: ")
    species = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")

    pets[new_id] = {name: {"Вид питомца": species, "Возраст питомца": age, "Имя владельца": owner}}

def read(pet_id):
    pet = get_pet(pet_id)
    if pet is not None:
        for name, info in pet.items():
            print(f"Это {info['Вид питомца']} по кличке \"{name}\". Возраст питомца: {info['Возраст питомца']} {get_suffix(info['Возраст питомца'])}. Имя владельца: {info['Имя владельца']}")
    else:
        print("Питомец не найден.")

def update(pet_id):
    pet = get_pet(pet_id)
    if pet is not None:
        name = input("Введите новое имя питомца: ")
        species = input("Введите новый вид питомца: ")
        age = int(input("Введите новый возраст питомца: "))
        owner = input("Введите новое имя владельца: ")

        pets[pet_id] = {name: {"Вид питомца": species, "Возраст питомца": age, "Имя владельца": owner}}
    else:
        print("Питомец не найден.")

def delete(pet_id):
    if pet_id in pets:
        del pets[pet_id]
        print("Запись о питомце удалена.")
    else:
        print("Питомец не найден.")

def get_pet(pet_id):
    return pets.get(pet_id)

def get_suffix(age):
    if 11 <= age % 100 <= 14:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif age % 10 in [2, 3, 4]:
        return "года"
    else:
        return "лет"

def pets_list():
    for pet_id, pet in pets.items():
        for name, info in pet.items():
            print(f"{pet_id}: {name} - {info['Вид питомца']}, {info['Возраст питомца']} {get_suffix(info['Возраст питомца'])}, Владелец: {info['Имя владельца']}")


def main():
    while True:
        command = input("Введите команду (factorial, create, read, update, delete, list, stop): ")
        if command == 'stop':
            break
        elif command == 'factorial':
            num = int(input("Введите натуральное число: "))
            result = factorial_list(num)
            print(result)
        elif command == 'create':
            create()
        elif command == 'read':
            pet_id = int(input("Введите ID питомца: "))
            read(pet_id)
        elif command == 'update':
            pet_id = int(input("Введите ID питомца: "))
            update(pet_id)
        elif command == 'delete':
            pet_id = int(input("Введите ID питомца: "))
            delete(pet_id)
        elif command == 'list':
            pets_list()
        else:
            print("Неизвестная команда.")

if __name__ == "__main__":
    main()
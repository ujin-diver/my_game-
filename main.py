from abc import ABC, abstractmethod

# === Шаг 1: Абстрактный класс для оружия ===
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# === Шаг 2: Конкретные типы оружия ===
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец стреляет из лука."

class Axe(Weapon):  # можно легко добавить новый тип оружия
    def attack(self):
        return "Боец наносит сокрушительный удар топором."

# === Класс монстра ===
class Monster:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def take_damage(self):
        self.health = 0
        return f"Монстр {self.name} побежден!"

# === Шаг 3: Класс бойца ===
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает новое оружие: {type(weapon).__name__}")

    def attack(self, monster: Monster):
        if self.weapon:
            print(self.weapon.attack())
            print(monster.take_damage())
        else:
            print("У бойца нет оружия!")

# === Шаг 4: Демонстрация боя ===
def main():
    # создаём бойца и монстра
    fighter = Fighter("Артур")
    monster = Monster("Гоблин")

    # выбираем меч
    fighter.change_weapon(Sword())
    fighter.attack(monster)

    print("\n--- Новый бой ---\n")

    # новый монстр и новое оружие
    monster2 = Monster("Орк")
    fighter.change_weapon(Bow())
    fighter.attack(monster2)

    print("\n--- Добавим новый тип оружия ---\n")

    # снова новый монстр и ещё одно оружие
    monster3 = Monster("Тролль")
    fighter.change_weapon(Axe())
    fighter.attack(monster3)

if __name__ == "__main__":
    main()

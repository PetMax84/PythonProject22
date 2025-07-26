import random
import time


class Hero:
    """Класс героя для игры 'Битва героев'"""

    def __init__(self, name, health=100, attack_power=20):
        """
        Инициализация героя

        Args:
            name (str): Имя героя
            health (int): Здоровье героя (по умолчанию 100)
            attack_power (int): Сила удара героя (по умолчанию 20)
        """
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        """
        Атакует другого героя

        Args:
            other (Hero): Другой герой, который получает урон
        """
        # Добавляем немного случайности в атаку
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        other.health -= damage
        print(f"⚔️ {self.name} атакует {other.name} и наносит {damage} урона!")

    def is_alive(self):
        """
        Проверяет, жив ли герой

        Returns:
            bool: True если здоровье больше 0, иначе False
        """
        return self.health > 0


class Game:
    """Класс игры 'Битва героев'"""

    def __init__(self, player_name):
        """
        Инициализация игры

        Args:
            player_name (str): Имя игрока
        """
        self.player = Hero(player_name, health=100, attack_power=20)
        # Компьютер с немного случайными характеристиками
        self.computer = Hero("Компьютер",
                             health=random.randint(90, 110),
                             attack_power=random.randint(18, 25))

    def start(self):
        """Начинает игру"""
        print("⚔️" + "=" * 48 + "⚔️")
        print("           БИТВА ГЕРОЕВ")
        print("⚔️" + "=" * 48 + "⚔️")
        print(f"\nИгрок: {self.player.name}")
        print(f"Здоровье: {self.player.health} | Сила удара: {self.player.attack_power}")
        print(f"\nПротивник: {self.computer.name}")
        print(f"Здоровье: {self.computer.health} | Сила удара: {self.computer.attack_power}")
        print("\n" + "🔥" + "-" * 48 + "🔥")

        round_num = 1

        # Основной игровой цикл
        while self.player.is_alive() and self.computer.is_alive():
            print(f"\n🔥 Раунд {round_num}")
            print("=" * 30)

            # Ход игрока
            input(f"\nНажмите Enter, чтобы атаковать...")
            self.player.attack(self.computer)

            if self.computer.is_alive():
                print(f"💙 У {self.computer.name} осталось {self.computer.health} здоровья")
            else:
                print(f"💀 {self.computer.name} погиб!")
                break

            print("-" * 30)

            # Ход компьютера
            time.sleep(1)  # Пауза для драматизма
            self.computer.attack(self.player)

            if self.player.is_alive():
                print(f"💚 У {self.player.name} осталось {self.player.health} здоровья")
            else:
                print(f"💀 {self.player.name} погиб!")
                break

            time.sleep(1)  # Пауза между раундами
            round_num += 1

            # Предотвращаем слишком долгую игру
            if round_num > 30:
                print("\n🕐 Игра слишком затянулась! Объявляется ничья!")
                return

        # Объявление победителя
        print("\n" + "🏆" + "=" * 48 + "🏆")
        if self.player.is_alive() and not self.computer.is_alive():
            print(f"🎉 ПОБЕДИЛ {self.player.name.upper()}! 🎉")
        elif self.computer.is_alive() and not self.player.is_alive():
            print(f"💻 ПОБЕДИЛ {self.computer.name.upper()}! 💻")
        elif not self.player.is_alive() and not self.computer.is_alive():
            print("🤝 Оба героя пали в бою! Ничья! 🤝")
        else:
            print("🤝 Ничья по времени! 🤝")
        print("🏆" + "=" * 48 + "🏆")


def main():
    """Главная функция игры"""
    print("🎮 Добро пожаловать в Битву Героев! 🎮")
    print("-" * 40)

    while True:
        player_name = input("Введите имя вашего героя: ").strip()

        if not player_name:
            print("Пожалуйста, введите имя!")
            continue
        else:
            break

    # Создание и запуск игры
    game = Game(player_name)

    try:
        game.start()
    except KeyboardInterrupt:
        print("\n\n👋 Игра прервана пользователем. До свидания!")
        return
    except Exception as e:
        print(f"\n❌ Произошла ошибка: {e}")
        print("Пожалуйста, сообщите об этой ошибке разработчику.")
        return

    # Предложение сыграть еще раз
    while True:
        play_again = input("\nХотите сыграть еще раз? (да/нет): ").lower().strip()
        if play_again in ['да', 'yes', 'y', 'д', 'так']:
            main()
            break
        elif play_again in ['нет', 'no', 'n', 'ні', 'н']:
            print("👋 Спасибо за игру! До встречи!")
            break
        else:
            print("Пожалуйста, ответьте 'да' или 'нет'")


# Запуск игры
if __name__ == "__main__":
    main()
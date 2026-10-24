# Проект FitLife - MVP версия 1.0.1

WATER_RATIO = 0.03  # л/кг
# 1. Знакомство
# user_name - имя пользователя
print("Рады приветствовать вас в нашем приложении FitLife!")
user_name = input("Как можно к вам обращаться? ")
user_age = int(input(f"{user_name}, укажите, пожалуйста, ваш возраст: "))

# 2. Сбор данных
user_weight = float(input(f"{user_name}, укажите, пожалуйста, ваш вес, кг: "))
user_height = float(input(f"{user_name}, укажите, пожалуйста, ваш рост, м: "))

# 3. Логика расчетов
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = user_weight / user_height ** 2

# Подсчет воды: вес * коэффициент
water_needed = user_weight * WATER_RATIO

# 4. Вывод результата
print(f"Уважаемый пользователь, {user_name}\n"
      f"Ваш возраст: {user_age}. ИМТ равен {bmi:.1f)}.\n"
      f"Рекомендуемая норма воды: {water_needed:.1f} л. в день\n"
      f"Расчет окончен. Будьте здоровы!")

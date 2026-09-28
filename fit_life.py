# ИИ Исправил: разбиты длинные строки для PEP 8
print('Приветствую! Я программа FitLife!')
# Использовала ИИ, чтобы больше понять про f-строки.
# В написании самого кода ИИ не применялся.
user_name = input('Давайте познакомимся! Как вас зовут? ')
print(f'Рад знакомству, {user_name}!')

user_age = int(input(f'{user_name}, сколько вам лет? '))

user_weight = float(
    input(
        f'{user_name}, ваш вес? '
        'Укажите в килограммах. Используйте точку, например 65.5.'
    )
)

user_height = float(
    input(
        f'{user_name}, сколько вы ростом? '
        'Укажите в метрах. Используйте точку.'
    )
)

# Расчёт индекса массы тела
bmi = user_weight / (user_height ** 2)
# Расчёт нормы воды
WATER_PER_KG = 30
water_ml = user_weight * WATER_PER_KG
WATER_PER_LITER = 1000
water_l = water_ml / WATER_PER_LITER

print(f'{user_name}, ваш отчёт готов!')
print(f'Данные пользователя: {user_name}, {user_age}')
if 18.5 <= bmi <= 24.9:
    print(f"{bmi:.1f} Норма")
elif 17 <= bmi <= 18.4:
    print(f"{bmi:.1f} Легкий дефицит")
elif 16 <= bmi <= 16.9:
    print(f"{bmi:.1f} Умеренный дефицит")
elif bmi < 16:
    print(f"{bmi:.1f} Выраженный дефицит массы")
elif 25 <= bmi <= 29.9:
    print(f"{bmi:.1f} Избыточная масса")
elif 30 <= bmi <= 34.9:
    print(f"{bmi:.1f} Ожирение I степени")
elif 35 <= bmi <= 39.9:
    print(f"{bmi:.1f} Ожирение II степени")
elif bmi >= 40:
    print(f"{bmi:.1f} Ожирение III степени")
print(f"Ваша норма воды в сутки: {water_l:.2f} л")
print('Отсчет окончен. Помните, в здоровом теле - здоровый дух!')

WATER_PER_KG = 30
WATER_PER_LITER = 1000


def calculation_bmi():
    """Рассчитывает ИМТ и норму воды, запрашивает данные у пользователя.

    Возвращает: имя, возраст, ИМТ, категория ИМТ, норма воды в литрах.
    """
    print('Приветствую! Я программа FitLife!')
    user_name = input('Давайте познакомимся! Как вас зовут? ')
    print(f'Рад знакомству, {user_name}!')

    user_age = int(input(f'{user_name}, сколько вам лет? '))

    user_weight = float(
        input(
            f'{user_name}, ваш вес? \n'
            'Укажите в килограммах.Например: 80.5 \n'
        ).replace(',', '.')
    )
    user_height = float(
        input(
            f'{user_name}, сколько вы ростом? \n'
            'Укажите в метрах. Например: 1.75 \n'
        ).replace(',', '.')
    )
    bmi = user_weight / (user_height ** 2)

    if 18.5 <= bmi < 25:
        bmi_category = 'Норма'
    elif 17 <= bmi < 18.5:
        bmi_category = 'Легкий дефицит'
    elif 16 <= bmi < 17:
        bmi_category = 'Умеренный дефицит'
    elif bmi < 16:
        bmi_category = 'Выраженный дефицит массы'
    elif 25 <= bmi < 30:
        bmi_category = 'Избыточная масса'
    elif 30 <= bmi < 35:
        bmi_category = 'Ожирение I степени'
    elif 35 <= bmi < 40:
        bmi_category = 'Ожирение II степени'
    elif bmi >= 40:
        bmi_category = 'Ожирение III степени'
    water_ml = user_weight * WATER_PER_KG
    water_l = water_ml / WATER_PER_LITER
    return user_name, user_age, bmi, bmi_category, water_l


if __name__ == '__main__':
    user_name, user_age, bmi, bmi_category, water_l = calculation_bmi()

    print(
        f'{user_name}, ваш отчёт готов! \n'
        f'Данные пользователя: {user_name}, {user_age} \n'
        f'ИМТ {bmi:.1f} - {bmi_category} \n'
        f'Ваша норма воды в сутки: {water_l:.2f} л \n'
        'Отсчет окончен. Помните, в здоровом теле - здоровый дух!',
    )

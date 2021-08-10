# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
#   имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def user_data(first_name, last_name, birth_year, city, email, t_number):
    return f"Имя - {first_name} // Фамилия - {last_name} // Год рождения - {birth_year} " \
           f"// Город проживания - {city} // E-mail - {email} // Номер телефона - {t_number}"


print("Введите Ваши данные")
result = user_data(first_name=input("Имя: "),
                   last_name=input("Фамилия: "),
                   birth_year=input("Год рождения: "),
                   city=input("Город проживания: "),
                   email=input("E-mail: "),
                   t_number=input("Номер телефона: "))
print(result)

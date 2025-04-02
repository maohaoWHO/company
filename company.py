"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.
13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

#1. Вывести названия всех отделов
def print_department_names(list_of_departments):
    print('1 task')
    for department in list_of_departments:
        print(department['title'])
    print()

#2. Вывести имена всех сотрудников компании.
def print_all_employees_names(list_of_departments):
    print('2 task')
    for department in list_of_departments:
        for workers in department["employers"]:
            print(workers["first_name"])
    print()

#3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
def print_employees_with_departments(list_of_departments):
    print('3 task')
    for department in list_of_departments:
        for workers in department["employers"]:
            print(f'{workers["first_name"]} работает в {department["title"]}')
    print()

#4. Вывести имена всех сотрудников компании, которые получают больше 100к.
def print_high_salary_employees(list_of_departments, min_salary):
    print('4 task')
    for department in list_of_departments:
        for workers in department["employers"]:
            if workers["salary_rub"] > min_salary:
                print(f'{workers["first_name"]} получает больше 100.000')
    print()

#5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
def print_low_salary_employees(list_of_departments, max_salary):
    print('5 task')
    for department in list_of_departments:
        for workers in department["employers"]:
            if workers["salary_rub"] < max_salary:
                print(workers["position"])
    print()

#6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
def print_department_expenses(list_of_departments):
    print('6 task')
    for department in list_of_departments:
        whole_salary = 0
        for workers in department["employers"]:
            whole_salary += workers["salary_rub"]
        print(f'На {department["title"]} в месяц уходит {whole_salary} рублей.')
    print()

#Второй уровень:

#7. Вывести названия отделов с указанием минимальной зарплаты в нём.
def get_departments_with_min_salary(list_of_departments):
    print('7 task')
    for department in list_of_departments:
        department_salary = []
        for workers in department["employers"]:
            department_salary.append(workers["salary_rub"])
        print(f"В {department['title']} минимальная зарплата составляет {min(department_salary)} рублей.")
    print()

#8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
def get_departments_salary_stats(list_of_departments):
    print('8 task')
    for departments in list_of_departments:
        department_salary = []
        for workers in departments["employers"]:
            department_salary.append(workers["salary_rub"])
        print(f"В отделе {departments['title']}:\nминимальная зарплата: {min(department_salary)}"
            f" рублей\nсредняя зарплата: {sum(department_salary)/len(department_salary)}"
            f" рублей\nмаксимальная зарплата: {max(department_salary)} рублей")
    print()

#9. Вывести среднюю зарплату по всей компании.
def calculate_company_avg_salary(list_of_departments):
    print('9 task')
    department_salary = []
    for department in list_of_departments:
        for workers in department["employers"]:
            department_salary.append(workers["salary_rub"])
    print(f'Средняя зарплата по компании составляет {sum(department_salary)/len(department_salary)} рублей.')
    print()

#10. Вывести названия должностей, которые получают больше 90к без повторений.
def get_unique_high_paid_positions(list_of_departments, min_salary):
    print('10 task')# не работает корректно
    workers_90k = set()
    for department in list_of_departments:
        for workers in department["employers"]:
            if workers["salary_rub"] >= min_salary:
                workers_90k.add(workers["position"])
    print('Зарплата на следующих позициях составляет более 90.000 рублей:')
    print(*workers_90k)
    print()

#11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
def calculate_female_avg_salary_by_dept(list_of_departments):
    print('11 task')

    girls_workers = ["Michelle", "Nicole", "Christina", "Caitlin"]

    for department in list_of_departments:
        girls_salary = []
        for workers in department["employers"]:
            if workers["first_name"] in girls_workers:
                girls_salary.append(workers["salary_rub"])
        print(f"Средняя зарплата женщин в {department['title']}"
            f" составляет {sum(girls_salary)/len(girls_salary):.2f} рублей.")
    print()

#12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
def get_names_with_vowel_lastnames(list_of_departments):
    print('12 task')
    vowels = 'aeiouy'
    names_ending_with_vowels = set()
    for department in list_of_departments:
        for workers in department["employers"]:
            if workers["last_name"].lower()[-1] in vowels:
                names_ending_with_vowels.add(workers["first_name"])
    print('Фамилии следующих сотрудников заканчиваются на гласные:')
    print(*names_ending_with_vowels)
    print()

if __name__ == '__main__':
    print_department_names(departments)
    print_all_employees_names(departments)
    print_employees_with_departments(departments)
    print_high_salary_employees(departments, min_salary = 100000)
    print_low_salary_employees(departments, max_salary = 80000)
    print_department_expenses(departments)
    get_departments_with_min_salary(departments)
    get_departments_salary_stats(departments)
    calculate_company_avg_salary(departments)
    get_unique_high_paid_positions(departments, min_salary = 90000)
    calculate_female_avg_salary_by_dept(departments)
    get_names_with_vowel_lastnames(departments)
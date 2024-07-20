print("Sistema vacacional de Rappi")
assist_dempartment = 1
logistic_department = 2
rh_depatment = 3
name = input("Ingrese su nombre por favor: ")
clave = int(input("Ingrese su clave: "))


def ask_for_worked_years():
    years = int(input("¿Cuantos años lleva trabajando en la empresa?: "))
    return years

def print_vacations_days(name, days):
    if days == 0:
        print(f'{name} have not vacations days T.T')
    else:
        print(f'{name} have {days} vacations days :)')

if clave == assist_dempartment:
    years= ask_for_worked_years()
    if years == 1:
        days = 6
        print_vacations_days(name, days)
    elif years >= 2 and years <= 6:
        days = 14
        print_vacations_days(name, days)
    elif years >= 7:
        days = 20
        print_vacations_days(name, days)
    else:
        days = 0
        print_vacations_days(name, days)
elif clave == logistic_department:
    years= ask_for_worked_years()
    if years == 1:
        days = 7
        print_vacations_days(name, days)
    elif years >= 2 and years <= 6:
        days = 15
        print_vacations_days(name, days)
    elif years >= 7:
        days = 22
        print_vacations_days(name, days)
    else:
        days = 0
        print_vacations_days(name, days)
elif clave == rh_depatment:
    years= ask_for_worked_years()
    if years == 1:
        days = 10
        print_vacations_days(name, days)
    elif years >= 2 and years <= 6:
        days = 20
        print_vacations_days(name, days)
    elif years >= 7:
        days = 30
        print_vacations_days(name, days)
    else:
        days = 0
        print_vacations_days(name, days)
else:  
    print("La clave que usted marco no se encuentra en este servidor")



    

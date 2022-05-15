"""
Каждый класс реализовать в отдельном модуле, импортируя их в производные модули.
Создать класс Person с полями имя, фамилия, возраст. Добавить конструктор класса.
Создать производный от Person класс Doctor. Новые поля: номер удостоверения, специальность, список текущих
    пациентов (словарь вида номер медицинской книжки: ФИ пациента). Определить конструктор, с вызовом родительского
    конструктора. Определить функции добавления нового пациента, удаления выписанного, форматированной печати
    всех пациентов. Переопределить метод преобразования в строку для печати основной информации (ФИ, возраст,
    номер удостоверения, специальность).
Создать производный от Person класс Nurse. Новые поля: номер удостоверения, отделение работы, график работы
    (словарь вида день недели: часы работы). Определить конструктор, с вызовом родительского конструктора.
    Определить функции изменения отделения, добавления, удаления и изменения графика работы. Переопределить
    метод преобразования в строку для печати основной информации (ФИ, возраст, номер удостоверения, отделение).
Создать класс Hospital Поля: название больницы, адрес, список врачей (список экземпляров класса Doctor),
    список медсестер (список экземпляров класса Nurse). Определить конструктор. Переопределить метод преобразования
    в строку для печати всей информации о больнице (с использованием переопределения в классах Doctor и Nurse).
    Переопределить методы получения количества врачей функцией len, получения врача по индексу, изменения
    по индексу, удаления по индексу (пусть номера врачей считаются с 1, а индекс 0 – список всех медсестер).
    Переопределить операции + и - для добавления или удаления врача. Добавить функцию создания txt-файла и
    записи всей информации в него (в том числе пациентов врачей и графика работы медсестер).
Предусмотреть хотя бы в 3 местах обработку возможных исключений.
В каждом модуле провести подробное тестирование всех создаваемых объектов и функций.
"""

class Person:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class Doctor(Person):

    def __init__(self, licence_id, occupation):
        super().__init__()
        self.licence_id = license_id
        self.occupation = occupation
        self.patients = {}
        self.doctors = []
        self.doctors.append(self)


    #List all patients
    def printAll(self):
        for var in self.patients:
            print(var)


    #Add new patient
    def addNewPatient(self):
        x = input('Print patient name: ')
        y = input('Print patient surname: ')
        self.patients[f'Patient {len(self.patients.items()) + 1}'] = x+' '+y


    #Remove patient
    def removePatient(self):
        self.printAll()
        x = input('What patient do you want to discharge? (num): ')
        self.patients.pop(f'Patient {x}')
        print('Patient {x} discharged!')


    #Info about Doctor
    def printInfo(self):
        print(f'Name: {self.name} {self.surname}')
        print(f'Age: {self.age}')
        print(f'Licence ID: {self.licence_id}')
        print(f'Occupation: {self.occupation}')


class Nurse(Person):

    def __init__(self, licence_id, ward, schedule):
        super().__init__()
        self.licence_id = licence_id
        self.ward = ward
        self.schedule = schedule
        self.nurses = []
        self.nurses.append(self)

        self.schedule = {
        'Monday': '-',
        'Tuesday': '-',
        'Wednesday': '-',
        'Thursday': '-',
        'Friday': '-',
        'Saturday': '-',
        'Sunday': '-'
        }


    #Ward change
    def wardChange(self):
        x = input('Print new ward for the nurse: ')
        self.ward = x


    #scheduleChange
    def scheduleChange(self):
        absent = True

        while absent:
            x = input('What day to you want to edit?: ')
            y = input('Enter new working hours: ')

            for var in len(self.schedule.items())
                if x in self.schedule:
                    absent = False
                    self.schedule[x] = y
                else:
                    print("There is no such day!")


    #scheduleChange
    def scheduleChange(self):
        absent = True

        while absent:
            x = input('What day to you want to remove?:' )

            for var in len(self.schedule.items())
                if x in self.schedule:
                    absent = False
                    self.schedule.pop(x)
                else:
                    print("There is no such day!")


    #Info about Doctor
    def printInfo(self):
        print(f'Name: {self.name} {self.surname}')
        print(f'Age: {self.age}')
        print(f'Licence ID: {self.licence_id}')
        print(f'Ward: {self.ward}')


class Hospital:

    #def __init__(self, hospital_name, address, doctors, nurses):
    #    super().__init__()
    #    self.hospital_name = hospital_name
    #    self.address = address
    #    self.employees = doctors.


def createObject():
    x1 = input()
    x2 = input()
    x = Hospital(x1, x2)

#ROADMAP:
#СОЗДАТЬ МЕТОД ПО ДОБАВЛЕНИЮ ОБЪЕКТА И ДОБАВЛЕНИЮ ЕГО АТРИБУТОВ В ЛИСТ КЛАССA HOSPITAL
#РАСПРЕДЕЛИТЬ КЛАССЫ ПО ОТДЛЕЛЬНЫМ ФАЙЛАМ
#НАПИСАТЬ МЕНЮ 

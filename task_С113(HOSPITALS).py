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

   hospital_name = ''
    address = ''
    doctors = []
    nurses = []

    def __init__(self, hospital_name, address, doctors, nurses):

        self.hospital_name = hospital_name
        self.address = address
        self.doctors = doctors
        self.nurses = nurses

    def print_info(self):
        print("Hospital title: " + self.hospital_name + "\n" + "Hospital address: " + self.address + "\n")
        print("Staff: ")
        print("Doctors: ")
        for var1 in self.doctors:
            print(var1.printInfo())
        print("Nurses: ")
        for var2 in self.nurses:
            print(var2.printInfo())

    def len(self):
        return len(self.doctors)

    def get_doctor(self, index):
        return self.doctors[index].printInfo()
#добавить нужно вмонтировать меню выбора, что именно нужно изменить

    def edit_doctor(self, index):
        while True:
            print("Select change: ")
            print("\t" + "1. Doctor's name")
            print("\t" + "2. Doctor's surname")
            print("\t" + "3. Doctor's age")
            print("\t" + "4. Doctor's licence_id")
            print("\t" + "5. Doctor's occupation")
            print("\t" + "6. Patients")
            print("\t" + "7. Exit")
            if input() == 1:
                self.doctors[index].name = input("Enter new Doctor's name")
            if input() == 2:
                self.doctors[index].surname = input("Enter new Doctor's surname")
            if input() == 3:
                self.doctors[index].age = int(input("Enter new Doctor's age"))
            if input() == 4:
                self.doctors[index].licence_id = int(input("Enter new Doctor's licence_id"))
            if input() == 5:
                self.doctors[index].occupation = int(input("Enter new Doctor's occupation"))
            if input() == 6:
                print("Select change: ")
                print("\t" + "1. Remove a patient")
                print("\t" + "2. Add a patient")
                if input() == 1:
                    self.doctors[index].addNewPatient()
                if input() == 2:
                    self.doctors[index].removePatient()
            if input() == 7:
                break
 def edit_nurses(self,index):
        while True:
            print("Select change: ")
            print("\t" + "1. Nurse's name")
            print("\t" + "2. Nurse's surname")
            print("\t" + "3. Nurse's age")
            print("\t" + "4. Nurse's licence_id")
            print("\t" + "5. Nurse's ward")
            print("\t" + "6. Nurse's schedule")
            print("\t" + "7. Exit")
            if input() == 1:
                self.doctors[index].name = input("Enter new Nurse's name")
            if input() == 2:
                self.doctors[index].surname = input("Enter new Nurse's surname")
            if input() == 3:
                self.doctors[index].age = int(input("Enter new Nurse's age"))
            # if input() == 4:
            #    // self.nurses[index]. = int(input("Enter new Nurse's licence_id"))
            # if input() == 5:
            #     self.doctors[index].occupation = int(input("Enter new Nurse's ward"))
            # if input() == 6:
            #     print("Select change: ")
            #     print("\t" + "1. Remove a schedule")
            #     print("\t" + "2. Add a schedule")
            #     if input() == 1:
            #         self.nurses[index].addNewPatient()
            #     if input() == 2:
            #         self.nurses[index].removePatient()
            if input() == 7:
                break

    def remove_doctor(self, index):
        self.doctors.remove(index)


    def remove_nurses(self,index):
        self.nurses.remove(index)

    def __add__(self, others):
        flag = False
        if isinstance(others, Doctor):
            if self.doctors[0] == None:
                self.doctors[1] = others
                flag = True
            else:
                self.doctors.append(others)
                flag = True
        if isinstance(others, Nurse):
            self.nurses.append(others)
            flag = True
        if flag == False:
            print("Error object")

    def __sub__(self, other):
        self.doctors.remove(other)

    def write_in_file(self):
        with open('C:\\Users\\narko\\Desktop\\Hospital info.txt', 'w') as new_file:
            new_file.write(print_info + '\n')
            for var1 in self.doctors:
                new_file.write(var1.printAll() + "\n")
            for var2 in self.nurses:
                new_file.write(var2.schedule.items() + "\n")

#тестирование функионала
def test():
    x = Hospital('Glory Dungeon', 'Van street 69')
    x + Doctor('2323211231412', 'Ass Doctor')
    x.doctors[0].addNewPatient()
    x.print_info()

test()
#ROADMAP:
#СОЗДАТЬ МЕТОД ПО ДОБАВЛЕНИЮ ОБЪЕКТА И ДОБАВЛЕНИЮ ЕГО АТРИБУТОВ В ЛИСТ КЛАССA HOSPITAL
#РАСПРЕДЕЛИТЬ КЛАССЫ ПО ОТДЛЕЛЬНЫМ ФАЙЛАМ
#НАПИСАТЬ МЕНЮ 

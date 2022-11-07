class Person:
    def __init__(self, name, age=None, sex=None):
        self.name = name
        self.age = age
        self.sex = sex


class StoreEmployee(Person):
    def __init__(self, workplace, job_title, department, hourly_wage, **kwarp):
        super(StoreEmployee, self).__init__(**kwarp)
        self.workplace = workplace
        self.job_title = job_title
        self.department = department
        self.hourly_wage = hourly_wage
        self.hours_worked = 0
        self.to_receive = 0
    
    def workShift(self, duration):
        self.hours_worked = self.hours_worked + duration
        print(f'{self.name} worked a {duration} hour shift')
        
    def receivePaycheck(self):
        self.to_receive = self.hours_worked * self.hourly_wage
        print(f'{self.name} is to get paid {self.to_receive} DKK for {self.hours_worked} hours of work')


class Student(Person):
    def __init__(self, study_program, **kwarp):
        super(Student, self).__init__(**kwarp)
        self.study_program = study_program
    
    def study(self, duration, intensity, course):
        print(f'{self.name} has studied {intensity} for {duration} hours. He has studies for the {course}-course')


class StudentAndEmployee(Person):
    def __init__(self, workplace, job_title, department, hourly_wage, study_program, **kwarp):
        super(StudentAndEmployee, self).__init__(**kwarp)
        self.workplace = workplace
        self.job_title = job_title
        self.department = department
        self.hourly_wage = hourly_wage
        self.hours_worked = 0
        self.to_receive = 0
        self.study_program = study_program

    def workShift(self, duration):
        self.hours_worked = self.hours_worked + duration
        print(f'{self.name} worked a {duration} hour shift')
        
    def receivePaycheck(self):
        self.to_receive = self.hours_worked * self.hourly_wage
        print(f'{self.name} is to get paid {self.to_receive} DKK for {self.hours_worked} hours of work')

    def study(self, duration, intensity, course):
        print(f'{self.study_program}-student {self.name} has studied {intensity} for {duration} hours. He studied for the {course}-course')


def main():
    jhd = StudentAndEmployee(
        name='Jonas', 
        age=20, 
        sex='Male', 
        workplace='Bilka',
        job_title='Sales Assistant', 
        department='Home & Living', 
        hourly_wage=125,
        study_program="IVK English" 
        )

    print(f'{jhd.name} is a {jhd.age} year old {jhd.sex} who works as a {jhd.job_title} in the {jhd.department} department at {jhd.workplace}')
    jhd.workShift(6)
    jhd.workShift(8)
    jhd.workShift(5)
    jhd.receivePaycheck()
    jhd.study(2, "intensely", "Pfth22")

if __name__ == '__main__':
    main()
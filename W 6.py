class person():
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Employee(person):
    def __init__(self, name, ID, dept_name, title, phone):
        self.ID = ID
        self.dept_name = dept_name
        self.title = title
        person.__init__(self, name, phone)


def main():
    emp1 = Employee("Susan Meyers", 47899, "Accounting",  "Vice President", "212-555-1212")
    emp2 = Employee("Mark Jones",   39119, "IT",           "Programmer",     "212-555-2468")
    emp3 = Employee("Joy Roger",    81774, "Operations",     "Engineer",     "212-555-9753")
    print("Name\t         ID Number\t     Department\t          Job Title\t       Phone")
    print(emp1.name, "\t", emp1.ID, "\t",    emp1.dept_name, "\t",   emp1.title, "",     emp1.phone)
    print(emp2.name, "\t", emp2.ID, "\t",    emp2.dept_name, "\t\t", emp2.title, "\t",   emp2.phone)
    print(emp3.name, "\t", emp3.ID, "\t",    emp3.dept_name, "\t",   emp3.title, "\t",   emp3.phone)


if __name__ == "__main__":
    main()

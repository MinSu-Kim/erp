from dto.Department import Department
from dto.Title import Title


class Employee():
    def __init__(self, **kwargs):
        self.__emp_no = int(kwargs['emp_no'])
        self.__emp_name = kwargs['emp_name'] if 'emp_name' in kwargs else None
        self.__gender = kwargs['gender'] if 'gender' in kwargs else None
        self.__dept = kwargs['dept'] if 'dept' in kwargs else None
        self.__manager = kwargs['manager'] if 'manager' in kwargs else None
        self.__salary = int(kwargs['salary']) if 'salary' in kwargs else None
        self.__title = kwargs['title'] if 'title' in kwargs else None
        self.__hire_date = kwargs['hire_date'] if 'hire_date' in kwargs else None
        self.__pic = len(kwargs['pic']) if 'pic' in kwargs else None
        self.__len = kwargs.__len__()

    @property
    def emp_no(self):
        return self.__emp_no

    @emp_no.setter
    def emp_no(self, emp_no):
        self.__emp_no = int(emp_no)

    @property
    def emp_name(self):
        return self.__emp_name

    @emp_name.setter
    def emp_name(self, emp_name):
        self.__emp_name = emp_name

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @property
    def dept(self):
        return self.__dept

    @dept.setter
    def dept(self, dept):
        self.__dept = dept;

    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, manager):
        self.__manager = manager

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = int(salary)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def hire_date(self):
        return self.__hire_date

    @hire_date.setter
    def hire_date(self, hire_date):
        self.__hire_date = hire_date

    @property
    def pic(self):
        return self.__pic

    @pic.setter
    def pic(self, pic):
        self.__pic = pic

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __iter__(self):
        return (i for i in (
        self.__emp_no, self.__emp_name, self.__gender, self.__dept, self.__manager, self.__salary, self.__title,
        self.__hire_date))

    def __repr__(self) -> str:
        class_name = type(self).__name__
        str_format = '{}('
        for k in range(self.__len):
            str_format += '{!r},'
        str_format = str_format[:len(str_format) - 1] + ')'
        return str_format.format(class_name, *self)
        # return '{}({!r}, {!r}, {!r}, {!r}, {!r}, {!r}, {!r}, {!r})'.format(class_name, *self)

    def __hash__(self):
        return hash(self.__emp_no) ^ hash(self.__emp_name)


if __name__ == "__main__":
    kargs = {'emp_no': 1, 'emp_name': '김민수', 'gender': True, 'dept': Department(dept_no=1),
             'manager': Employee(**{'emp_no': 1}),
             'salary': 1500000, 'title': Title(title_no=1), 'hire_date': '2020-02-18'}

    empList = [Employee(**kargs), Employee(**kargs)]

    [print(e) for e in empList]

    print(empList[0] == empList[1])

    print(Employee(**{'emp_no': 1, 'emp_name': '김민수'}))

    # print(empList[0].__dict__)
    for key, value in empList[0].__dict__.items():
        print(key, type(value), value)
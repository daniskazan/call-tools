import re
from dataclasses import dataclass
from typing import List
from itertools import groupby


@dataclass
class Employee:
    name: str
    hours: int


def get_data() -> List:
    employees = []
    try:
        while True:
            data = re.split(pattern=r'\s(?=\d+(?!\S))', string=input())
            employees.append(Employee(name=data[0], hours=int(data[1])))
    except KeyboardInterrupt:
        employees.sort(key=lambda emp: emp.name)  # noqa
        return employees

def main():
    employees: List[Employee] = get_data()

    #  сгруппируем Employee по имени
    grouped_objects = {}
    for key, group in groupby(employees, lambda obj: obj.name):
        grouped_objects[key] = list(group)


    for k, v in grouped_objects.items():
        print(k, ", ".join(list(str(emp.hours) for emp in v)), f"Sum: {sum(list(emp.hours for emp in v))}")


if __name__ == '__main__':
    """
    Input:
    Андрей 9
    Василий 11
    Роман 7
    X Æ A-12 45
    Иван Петров 3
    Андрей 31
    
    Output:
    X Æ A-12 45 Sum: 45
    Андрей 9, 31 Sum: 40
    Василий 11 Sum: 11
    Иван Петров 3 Sum: 3
    Роман 7 Sum: 7

    """
    main()

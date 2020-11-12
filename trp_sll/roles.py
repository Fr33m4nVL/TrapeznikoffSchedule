from rolepermissions.roles import AbstractUserRole

class Student(AbstractUserRole):
    available_permissions = {
        'CRUD_homework': True,
        'CRUD_answer': False,
        'CRUD_news': False,
        'CRUD_subject': True,
    }

class Headman(AbstractUserRole):
    available_permissions = {
        'Add_a_student': True,
        'Allow_to_add_homework': True,
        'Allow_to_add_answer': True,
        'CRUD_homework': True,
        'CRUD_answer': False,
        'CRUD_news': True,
        'CRUD_subject': True,
    }

class Teacher(AbstractUserRole):
    available_permissions = {
        'Add_a_student': True,
        'Assign_a_headman': True,
        'Allow_to_add_homework': True,
        'Allow_to_add_answer': True,
        'CRUD_homework': True,
        'CRUD_answer': True,
        'CRUD_news': True,
        'CRUD_subject': True,
        'CRUD_group': True,
    }
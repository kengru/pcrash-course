# Exercise 9-8. Creates an instance of another class when it's instanciated.

class User():
    def __init__(self, first_name, last_name, age, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.username = username

    def describe_user(self):
        print('\nUsername: ' + self.username)
        print('Name: ' + self.first_name + ' ' + self.last_name)
        print('Age: ' + str(self.age))

    def greet_user(self):
        print('Hello ' + self.first_name + ' ' + self.last_name + '!')

class Privileges():
    def __init__(self):
        self.privileges = ['write', 'delete', 'edit']

    def show_privileges(self):
        print('Your privileges are: ')
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self, first_name, last_name, age, username):
        super().__init__(first_name, last_name, age, username)
        self.privileges = Privileges()

admin = Admin('Mark', 'Twain', 122, 'mktwain')
admin.privileges.show_privileges()

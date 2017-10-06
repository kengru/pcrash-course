# Exercise 9-5. Setting and modifying attributes through methods.

class User():
    def __init__(self, first_name, last_name, age, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        print('\nUsername: ' + self.username)
        print('Name: ' + self.first_name + ' ' + self.last_name)
        print('Age: ' + str(self.age))

    def greet_user(self):
        print('Hello ' + self.first_name + ' ' + self.last_name + '!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('Mark', 'Twain', 122, 'mktwain')
user.increment_login_attempts()
user.increment_login_attempts()
print('Attempts: ' + str(user.login_attempts))
user.reset_login_attempts()
print('Attempts: ' + str(user.login_attempts))

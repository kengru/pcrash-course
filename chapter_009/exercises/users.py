# Exercise 9-3. A user class that greets an user.

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

user1 = User('Kendry', 'Grullon', 23, 'kengru')
user2 = User('Jack', 'Veneno', 60, 'jven')
user3 = User('Mark', 'Twain', 122, 'mktwain')

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()

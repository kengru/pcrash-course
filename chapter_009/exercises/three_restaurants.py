# Exercise 9-2. Creating some instances.

class Restaurant():
    """A restaurant class, has two values and two functions."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize values."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Printing the characteristics."""
        print('\nRestaurant name: ' + self.restaurant_name)
        print('Cuisine type: ' + self.cuisine_type)

    def open_restaurant(self):
        """Printing the status of the restaurant."""
        print('The ' + self.restaurant_name + ' is open!')

restaurant_1 = Restaurant('Gym Food', 'Proteins?')
restaurant_2 = Restaurant('Shushishu', 'Japanese')
restaurant_3 = Restaurant('Mangos', 'Hamburger')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

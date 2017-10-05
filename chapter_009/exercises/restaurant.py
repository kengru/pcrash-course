# Exercise 9-1. A Restaurant's class.

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

restaurant = Restaurant('Krusty Krab', 'Sushi')
print('Name: ' + restaurant.restaurant_name)
print('Type: ' + restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Exercise 9-4. Adding a default value to the restaurant.

class Restaurant():
    """A restaurant class, has two values and two functions."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize values."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Printing the characteristics."""
        print('\nRestaurant name: ' + self.restaurant_name)
        print('Cuisine type: ' + self.cuisine_type)

    def open_restaurant(self):
        """Printing the status of the restaurant."""
        print('The ' + self.restaurant_name + ' is open!')

    def set_number_served(self, number):
        """Sets the number served."""
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

restaurant = Restaurant('Krusty', 'Sea Food')
print('Number served: ' + str(restaurant.number_served))
restaurant.number_served = 10
print('Number served: ' + str(restaurant.number_served))
restaurant.set_number_served(15)
print('Number served: ' + str(restaurant.number_served))
restaurant.increment_number_served(15)
print('Number served: ' + str(restaurant.number_served))

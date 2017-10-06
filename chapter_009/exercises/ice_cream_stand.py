# Exercise 9-6. Inheritance.

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

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['pizza', 'vanilla', 'chocolate', 'strawberry']

    def show_flavors(self):
        print('Flavors are: ')
        for flavor in self.flavors:
            print(flavor)

ice_cream_stant = IceCreamStand('Icess', 'Ice Cream')
ice_cream_stant.show_flavors()

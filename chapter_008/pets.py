# Arguments on functions.

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + ' name is ' + pet_name.title() + '.')

describe_pet('harry', animal_type='hamster')
describe_pet(pet_name='willie')

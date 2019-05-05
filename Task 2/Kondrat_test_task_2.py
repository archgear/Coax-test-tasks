def answer():
    print('Q: What is the purpose of decorators?')
    print(
        "A: In practice decorators can be used to extend capabilities of functions from external libraries that can not "
        "\nbe modified or to simplify debugging."
        " Also it can be used in Django for some purposes but I've googled that and can't explain it :)\n")


def burger(func):
    def wrapper():
        print('Top bread \nVegetables')
        func()
        print('Sauce \nBottom bread')
    return wrapper


@burger
def patty():
    if vegeterian == 'N':
        print('Meat patty')
    elif vegeterian == 'Y':
        print('Tofu patty')

answer()

print('Example: You have a bar with burgers -  both vegeterian and with meat' )
vegeterian = input("Is client a vegeterian? Y/N :")
patty()

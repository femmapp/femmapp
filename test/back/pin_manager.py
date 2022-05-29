from src.back.Pin import Pin
from src.back.pin_manager import create_new_pin as create, review_pin as review, unreview_pin as unreview

def main():
    lista  = [True, False, True, True, True, False, True, False, True, True, False]
    create("Prova random", 1, lista, 41.40722263, 2.169302913, "Una descripció")
    review(7, 3, True)
    review(7, 3, False)
    unreview(7, 3, True)
    
    pin = Pin(11, "name", "description", "author_id", "latitude", "longitude")
    print(pin.id)
    pin.name = ("hola", "idk")
    print(pin.name)
    pin.name = ("bola", "author_id")
    print(pin.name)
    print(pin.description)
    pin.description = ("bola", "autr_id")
    print(pin.description)
    pin.description = ("bola", "author_id")
    print(pin.name)
    print(pin.author_id)
    print(pin.coordinates)
    pin.coordinates = ("hola", "bola", "hol")
    print(pin.coordinates)
    pin.coordinates = ("hola", "bola", "author_id")
    print(pin.coordinates)
    print(pin.attributes)
    print(pin['RedFlag'])
    print(pin['RedFlag'].__bool__())
    print(pin['RedFlag'].add_review(True).add_review(False).add_review(False))
    print(pin['RedFlag'].__bool__())

if __name__ == '__main__':
    main()
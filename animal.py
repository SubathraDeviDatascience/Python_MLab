def animal_sound(animal):
    switcher={
        'dog':'bark',
        'cat':'Meow',
        'cow':'maa'
    }
    return switcher.get(animal,"Unknown Sound")
print(animal_sound('dog'))
print(animal_sound('goat'))
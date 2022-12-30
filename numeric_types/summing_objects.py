def sum_objects(*objects):
    sum = 0
    for object in objects:
        if type(object) == int:
            sum += object
    return sum

print(sum_objects('hola', 1, 2, 5, 'cancion', (), [])) 
import average


def strings_operations( *strings ):
    strings_len = []

    for string in strings:
        strings_len.append(len(string))
        
    str_min_len = min(strings_len)
    str_max_len = max(strings_len)
    str_avg = average.average(*strings_len)

    return (str_min_len, str_max_len, str_avg)


# print(strings_operations('hola', 'desayuno', 'carrera', 'sistemas', 'medicina', 'esternocleidomastoideo', 'hi'))

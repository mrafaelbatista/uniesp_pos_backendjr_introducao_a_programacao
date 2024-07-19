temperaturas = [23, 24, 25, 26, 27, 28, 29, 30, 31, 32]


def temp_media(temperaturas:list) -> float:

    temperatura_acumulada = 0

    for temperatura in temperaturas:
        temperatura_acumulada += temperatura

    media = temperatura_acumulada / len(temperaturas)

    return media


def temp_max(temperaturas:list) -> float:

    temperatura_maxima = 0

    for temperatura in temperaturas:

        if temperatura_maxima < temperatura:
            temperatura_maxima = temperatura

    return temperatura_maxima


print(temp_media(temperaturas))
print(temp_max(temperaturas))



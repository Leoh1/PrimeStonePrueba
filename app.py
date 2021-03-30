# -*- coding: utf-8 -*-
def separator():
    print('\n********************************************************************\n')


def punto_1(number_array: list):
    """
    Recibe un arreglo de numeros y lo ordena ascendemente
    """
    assert isinstance(number_array, list), "El argumento no es una lista"

    print('Arreglo original: ', number_array)
    number_array.sort()
    print('Arreglo ordenado: ', number_array)


def punto_2(n: int) -> str:
    """
    Dado un número entero n, mayor que 0 y menor que 10, genera una cadena con 
    todas las posibles permutaciones de dígitos, entre 1 y n, separadas por coma
    """
    assert isinstance(n, int), "El argumento no es un entero"
    assert n > 0, "El numero es menor a 0"
    assert n < 10, "El numero es mayor a 10"
    import itertools

    number_array = [str(number) for number in range(1, n+1)]
    array_string = ''.join(number_array)
    tuple_permutations = itertools.permutations(array_string, n)
    string_permutations = [''.join(permutation)
                           for permutation in tuple_permutations]

    return ', '.join(string_permutations)


def punto_4(frame: str):
    """
    Presenta el número de led y valor de pulso en pantalla por cada bloque de la trama
    """
    assert isinstance(frame, str), "El argumento no es un string"

    packets = frame.split(' ')
    for packet in packets:
        translated_packet = translate_packet(packet)
        print('Paquete: ' + packet)
        print('Número de led:' + str(translated_packet[0]))
        print('Valor del pulso:' + str(translated_packet[1]))
        print('\n')


def translate_packet(packet: str):
    assert isinstance(packet, str), "El argumento no es un string"

    binary = hex_to_binary(packet)
    binary_led, binary_value = binary[:7], binary[7:]

    return binary_to_decimal(binary_led), binary_to_decimal(binary_value)


def hex_to_binary(hex: str):
    assert isinstance(hex, str), "El argumento no es un string"

    return bin(int(hex, 16))[2:]


def binary_to_decimal(binary: str):
    assert isinstance(binary, str), "El argumento no es un string"

    return int(binary, 2)


def main():
    # Punto 1
    separator()
    print('Punto 1:')
    number_array = [10, 2, 23, 24, 253, 26, 274, 80, 9,
                    103, 11, 102, 13, 414, 15, 316, 174, 18, 109, 20]
    punto_1(number_array)

    # Punto 2
    separator()
    print('Punto 2:')
    n = 4
    print(punto_2(n))

    # Punto 4
    separator()
    print('Punto 3:')
    frame = '58A6 FC89 BD1A 4313 1250 0F21 C89B D1A4'
    punto_4(frame)


if __name__ == "__main__":
    main()

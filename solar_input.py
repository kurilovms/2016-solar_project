# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                star = parse_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                planet = parse_parameters(line, planet)
                objects.append(planet)
            if object_type != 'star' and object_type != 'planet':
                print("Unknown space object")

    return objects


def parse_parameters(line, space_object):
    """Считывает данные о космическом объекте из строки.
    Входная строка должна иметь слеюущий формат:
    Type <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты объекта, (Vx, Vy) — скорость.
    Type это тип объекта -- Star или Planet.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    try:
        obj_type, r, color, m, x, y, Vx, Vy = line.split()
    except:
        raise TypeError("Non-valid line")
    obj_type = obj_type.lower()
    m = float(m)
    x = float(x)
    y = float(y)
    r = float(r)
    Vx = float(Vx)
    Vy = float(Vy)
    if obj_type == 'star':
        return Star(m, x, y, r, Vx, Vy, color)
    if obj_type == 'planet':
        return Planet(m, x, y, r, Vx, Vy, color)


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    output = open(output_filename, 'a')
    for obj in space_objects:
        data = obj.get_param()
        output.write(data)
    output.close()
    graphics(space_objects)


def graphics(space_objects):
    for obj in space_objects:
        speeds = obj.speeds
        times = obj.times
        cm = obj.cm

        fig, axs = plt.subplots(1, 3, figsize=(12, 5))

        #subplot 1
        axs[0].plot(times, speeds)
        axs[0].set_xlabel(r't, \text{с}')
        axs[0].set_ylabel(r'v, dfrac{\text{м}}{\text{с}}')
        axs[0].set_title(r'$(t)')
        axs[0].grid(True)

        #subplot 2
        axs[1].plot(times, cm)
        axs[1].set_xlabel(r't, \text{с}')
        axs[1].set_ylabel(r'r, \text{м}')
        axs[1].set_title(r'r(t)')
        axs[1].grid(True)

        #subplot 3
        axs[2].plot(speeds, cm)
        axs[2].set_xlabel(r'v, \dfrac{\text{м}}{\text{с}}')
        axs[2].set_ylabel(r'r, \text{м}')
        axs[2].set_title(r'v(r)')
        axs[2].grid(True)

        plt.show()


# FIXME: хорошо бы ещё сделать функцию, сохраняющую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")

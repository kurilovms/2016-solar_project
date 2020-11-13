# coding: utf-8
# license: GPLv3

G = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def save_data_for_graphics(space_objects, t):
    """Вычисляет положение центра масс и расстояние от него до каждого из тел.
    Сохраняет расстояние от центра масс, скорость и время для каждого из тел для построения графика.

    Параметры:
    **space_objects** — список объектов, которые воздействуют на тело.
    **time** - настоящее время.
    """
    x_cm = 0
    y_cm = 0
    thing_x = 0
    thing_y = 0
    mass_total = 0
    for obj in space_objects:
        thing_x += obj.x*obj.m
        thing_y += obj.y*obj.m
        mass_total += obj.m
    x_cm = thing_x/mass_total
    y_cm = thing_y/mass_total
    for obj in space_objects:
        obj.cm += [((obj.x - x_cm)**2 + (obj.y - y_cm)**2)**0.5]
        v = (obj.Vx**2 + obj.Vy**2)**0.5
        obj.speeds += [v]
        obj.times += [t]


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов системы.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body != obj:
            r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
            F = G*obj.m*body.m/(r**2)
            body.Fx += F*(obj.x - body.x)/r
            body.Fy += F*(obj.y - body.y)/r    


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx/body.m
    body.x += body.Vx*dt
    body.Vx += ax*dt
    ay = body.Fy/body.m
    body.y += body.Vy*dt
    body.Vy += ay*dt


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")

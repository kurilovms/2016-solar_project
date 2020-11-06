# coding: utf-8
# license: GPLv3


class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """
    def __init__(self):
        self.type = 'star'
        self.m = 0
        self.x = 0
        self.y = 0
        self.Vx = 0
        self.Vy = 0
        self.Fx = 0
        self.Fy = 0
        self.R = 5
        self.color = 'red'
        self.image = None

    def get_param(self):
        s = 'Star '
        s += str(self.R) + ' '
        s += self.color + ' '
        s += str(self.m) + ' '
        s += str(self.x) + ' '
        s += str(self.y) + ' '
        s += str(Vx) + ' '
        s += str(Vy)
        return s


class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """
    def __init__(self):
        self.type = 'planet'
        self.m = 0
        self.x = 0
        self.y = 0
        self.Vx = 0
        self.Vy = 0
        self.Fx = 0
        self.Fy = 0
        self.R = 5
        self.color = 'green'
        self.image = None

    def get_param(self):
        s = 'Planet '
        s += str(self.R) + ' '
        s += self.color + ' '
        s += str(self.m) + ' '
        s += str(self.x) + ' '
        s += str(self.y) + ' '
        s += str(Vx) + ' '
        s += str(Vy)
        return s

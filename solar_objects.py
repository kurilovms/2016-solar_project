# coding: utf-8
# license: GPLv3


class Object:
    """Тип данных, описывающий космический объект.
    Содержит массу, координаты, скорость объекта,
    а также его визуальный радиус в пикселах.
    """
    def __init__(self, m=0, x=0, y=0, R=5, Vx=0, Vy=0):
        self.m = m
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.Fx = 0
        self.Fy = 0
        self.R = R
        self.image = None
        self.cm = []
        self.times = []
        self.speeds = []

    def get(self):
        s = str(self.m) + ' '
        s += str(self.x) + ' '
        s += str(self.y) + ' '
        s += str(self.Vx) + ' '
        s += str(self.Vy) + '\n'
        return s


class Star(Object):
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """
    def __init__(self, m=0, x=0, y=0, R=5, Vx=0, Vy=0, color = 'red'):
        super().__init__(m, x, y, R, Vx, Vy)
        self.type = 'star'
        self.color = color

    def get_param(self):
        data = 'Star '
        data += str(self.R) + ' '
        data += str(self.color) + ' '
        data += self.get()
        return data


class Planet(Object):
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """
    def __init__(self, m=0, x=0, y=0, R=5, Vx=0, Vy=0, color = 'green'):
        super().__init__(m, x, y, R, Vx, Vy)
        self.type = 'planet'
        self.color = color

    def get_param(self):
        data = 'Planet '
        data += str(self.R) + ' '
        data += str(self.color) + ' '
        data += self.get()
        return data

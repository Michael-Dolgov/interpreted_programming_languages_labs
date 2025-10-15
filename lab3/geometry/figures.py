import abc
from typing import Self, Tuple


class EuclidFigure(abc.ABC):
    class Point:
        """(x,y) coords for Euclidean space"""
        def __init__(self, x: float, y: float) -> None:
            self.x = x
            self.y = y

    """Points in a clockwise direction in Euclidean space"""
    @abc.abstractmethod
    def calculate_area(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def move(self, dx: float, dy: float) -> None:
        """Move figure by dx, dy"""
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def compare(cls, figure1: Self, figure2: Self) -> int:
        """Compare areas of two figures"""
        fig1_area = figure1.calculate_area()
        fig2_area = figure2.calculate_area()
        if fig1_area > fig2_area:
            return 1
        elif fig1_area == fig2_area:
            return 0
        else:
            return -1


class Triangle(EuclidFigure):
    def __init__(self,
                 dot1: Tuple[float, float],
                 dot2: Tuple[float, float],
                 dot3: Tuple[float, float]) -> None:
        self.__dots = [self.Point(*dot1), self.Point(*dot2), self.Point(*dot3)]

    def move(self, dx: float, dy: float) -> None:
        for p in self.__dots:
            p.x += dx
            p.y += dy

    def calculate_area(self) -> float:
        """Calculates figure area by Heron's formula"""
        a = ((self.__dots[0].x - self.__dots[1].x)**2 + (self.__dots[0].y - self.__dots[1].y)**2) ** 0.5
        b = ((self.__dots[1].x - self.__dots[2].x)**2 + (self.__dots[1].y - self.__dots[2].y)**2) ** 0.5
        c = ((self.__dots[2].x - self.__dots[0].x)**2 + (self.__dots[2].y - self.__dots[0].y)**2) ** 0.5
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area


class Rectangle(EuclidFigure):
    def __init__(self,
                 dot1: Tuple[float, float],
                 dot2: Tuple[float, float],
                 dot3: Tuple[float, float],
                 dot4: Tuple[float, float]):
        self.__dots = [self.Point(*dot1), self.Point(*dot2),
                       self.Point(*dot3), self.Point(*dot4)]

    def move(self, dx: float, dy: float) -> None:
        for p in self.__dots:
            p.x += dx
            p.y += dy

    def calculate_area(self) -> float:
        ABx = self.__dots[1].x - self.__dots[0].x
        ABy = self.__dots[1].y - self.__dots[0].y
        ADx = self.__dots[3].x - self.__dots[0].x
        ADy = self.__dots[3].y - self.__dots[0].y
        area = abs(ABx * ADy - ABy * ADx)
        return area

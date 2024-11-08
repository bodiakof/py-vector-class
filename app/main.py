from __future__ import annotations
import math


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.coord_x = round(coordinate_x, 2)
        self.coord_y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.coord_x + other.coord_x,
            self.coord_y + other.coord_y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.coord_x - other.coord_x,
            self.coord_y - other.coord_y
        )

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(
                round(self.coord_x * other, 2),
                round(self.coord_y * other, 2)
            )
        elif isinstance(other, Vector):
            dot_product = (self.coord_x * other.coord_x
                           + self.coord_y * other.coord_y)
            return round(dot_product, 14)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[int | float, int | float],
            end_point: tuple[int | float, int | float]) -> Vector:
        point_1 = round(end_point[0] - start_point[0], 2)
        point_2 = round(end_point[1] - start_point[1], 2)
        return cls(point_1, point_2)

    def get_length(self) -> float:
        return round(math.sqrt(self.coord_x ** 2 + self.coord_y ** 2), 15)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(
            round(self.coord_x / length, 2),
            round(self.coord_y / length, 2)
        )

    def angle_between(self, other: Vector) -> float:
        dot_product = self * other
        cos_theta = dot_product / (self.get_length() * other.get_length())
        angle = math.degrees(math.acos(cos_theta))
        return round(angle)

    def get_angle(self) -> int:
        return int(math.degrees(math.acos(self.coord_y / self.get_length())))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x_new = (self.coord_x * math.cos(radians)
                 - self.coord_y * math.sin(radians))
        y_new = (self.coord_x * math.sin(radians)
                 + self.coord_y * math.cos(radians))
        return Vector(round(x_new, 2), round(y_new, 2))

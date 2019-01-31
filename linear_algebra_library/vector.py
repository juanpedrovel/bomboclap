import math
from decimal import Decimal, getcontext

getcontext().prec = 10
tolerance = 1e-6

class Vector:
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)


    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
    

    def times_scalar(self, scalar):
        new_coordinates = [x*scalar for x in self.coordinates]
        return Vector(new_coordinates)


    def magnitude(self):
        magnitude_of_vector = 0
        for i in self.coordinates:
            magnitude_of_vector += i ** 2
        return Decimal(math.sqrt(magnitude_of_vector))


    def normalized(self):
        magnitude_of_vector = self.magnitude()
        try:
            direction = Decimal('1.0') / magnitude_of_vector
            return self.times_scalar(direction)
        except ZeroDivisionError:
            raise ZeroDivisionError('Cannot normalize Zero Vector')
    

    def dot_product(self, v):
        product = sum([x*y for x,y in zip(self.coordinates, v.coordinates)])
        return product


    def angle_with(self, v, in_degrees = False):
        # returns angle between vectors in radians
        try:
            normalize1 = self.normalized()
            normalize2 = v.normalized()
            d_product = normalize1.dot_product(normalize2)
            d_product = MyDecimal(d_product).check_tolerance()
            in_radians = math.acos(d_product)
            if in_degrees == False:
                return in_radians
            else:
                return in_radians * 180 / math.pi
        except ZeroDivisionError:
            raise ZeroDivisionError('Angles cannot be computed with Zero Vector')


    def is_parallel(self, v):
        if self.is_zero() or v.is_zero():
           return True
        angle = self.angle_with(v)
        if abs(angle - 0) < tolerance or abs(angle - math.pi) < tolerance:
            return True
        return False


    def is_zero(self):
        return self.magnitude() < tolerance


    def is_orthogonal(self, v):
        return abs(self.dot_product(v)) <= tolerance

    
    def project_to(self, b):
        try:
            unit_vector_b = b.normalized()
            weight = self.dot_product(unit_vector_b)
            projection = unit_vector_b.times_scalar(weight)
            return projection
        except ZeroDivisionError:
            raise ZeroDivisionError('Cannot normalize Zero Vector')


    def component_orthogonal_to(self, b):
        try:
            projection = self.project_to(b)
            orthogonal_component = self.minus(projection) 
            return orthogonal_component
        except ZeroDivisionError:
            raise ZeroDivisionError('Cannot normalize Zero Vector')


    def cross_product(self, v):
        c_product = Vector([self.coordinates[1]*v.coordinates[2] - v.coordinates[1] * self.coordinates[2],
                        -(self.coordinates[0]*v.coordinates[2] - v.coordinates[0]*self.coordinates[2]),
                        self.coordinates[0]*v.coordinates[1] - v.coordinates[0] * self.coordinates[1]])
        return c_product
    

    def area_parallelogram(self, v):
        cross_product = self.cross_product(v)
        return cross_product.magnitude()


    def area_triangle(self, v):
        return self.area_parallelogram(v) / Decimal('2.0')

    def __iter__(self):
        return iter(self.coordinates)


    def __getitem__(self,index):
            return self.coordinates[index]


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    
    def __len__(self):
        return len(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates


class MyDecimal(Decimal):
    def check_tolerance(self):
        if abs(self) < tolerance:
            return Decimal('0')
        elif abs(self - 1) < tolerance:
            return Decimal('1')
        elif abs(1 + self) < tolerance:
            return Decimal('-1')
        return self


    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps
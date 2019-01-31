from decimal import Decimal, getcontext

from vector import Vector

getcontext().prec = 30
tolerance = 1e-6


class Line:

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = ['0']*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()


    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = ['0']*self.dimension

            initial_index = Line.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e


    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector

        try:
            initial_index = Line.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output


    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)


    def is_parallel(self, line2):
        return self.normal_vector.is_parallel(line2.normal_vector)

    def plus(self, line2):
        new_vector = self.normal_vector.plus(line2.normal_vector)
        new_constant_term = self.constant_term + line2.constant_term
        return Line(new_vector, new_constant_term)


    def __eq__(self, line2):
        if self.normal_vector.is_zero():
            if line2.normal_vector.is_zero():
                difference = self.constant_term - line2.constant_term
                return MyDecimal(difference).is_near_zero() 
            return False
        if line2.normal_vector.is_zero():
            return False

        if self.is_parallel(line2):
            #connect a point of each line and check if resulting vector is
            #orthogonal to the normal vectors of the lines
            vector_l1_to_l2 = line2.basepoint.minus(self.basepoint)
            if vector_l1_to_l2.is_orthogonal(self.normal_vector):
                return True
        return False

    def intersection(self, line2):
        try:
            #The first line can't have A = 0
            if self.normal_vector.coordinates[0] == 0:
                return line2.intersection(self)
            A, B = self.normal_vector.coordinates
            C, D = line2.normal_vector.coordinates
            k1 = self.constant_term
            k2 = line2.constant_term
            x = Decimal((D*k1 - B*k2) / (A*D - B*C))
            y = Decimal((-C*k1 + A*k2) / (A*D - B*C))
            return Vector([x, y])
        except:
            if self == line2:
                return 'Lines are Equal'
            return 'No Intersection, Lines are parallel'

class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps
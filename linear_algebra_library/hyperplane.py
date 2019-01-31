from decimal import Decimal, getcontext

from vector import Vector

getcontext().prec = 30
tolerance = 1e-6


class Hyperplane:

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, dimension=None,  normal_vector=None, constant_term=None):
        if not dimension and not normal_vector:
            raise Exception('Either dimension or vector must be provided')

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

            initial_index = Hyperplane.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Hyperplane.NO_NONZERO_ELTS_FOUND_MSG:
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
            initial_index = Hyperplane.first_nonzero_index(n)
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

    def times_scalar(self, scalar):
        self.normal_vector = self.normal_vector.times_scalar(scalar)
        self.constant_term *= scalar


    def plus(self, hyperplane2):
        new_vector = self.normal_vector.plus(hyperplane2.normal_vector)
        new_constant_term = self.constant_term + hyperplane2.constant_term
        return Hyperplane(new_vector, new_constant_term)

    def is_parallel(self, hyperplane2):
        return self.normal_vector.is_parallel(hyperplane2.normal_vector)


    def __eq__(self, hyperplane2):
        if self.normal_vector.is_zero():
            if hyperplane2.normal_vector.is_zero():
                difference = self.constant_term - hyperplane2.constant_term
                return MyDecimal(difference).is_near_zero() 
            return False
        if hyperplane2.normal_vector.is_zero():
            return False

        if self.is_parallel(hyperplane2):
            #connect a point of each hyperplane and check if resulting vector is
            #orthogonal to the normal vectors of the hyperplanes
            vector_p1_to_p2 = hyperplane2.basepoint.minus(self.basepoint)
            if vector_p1_to_p2.is_orthogonal(self.normal_vector):
                return True
        return False


    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Hyperplane.NO_NONZERO_ELTS_FOUND_MSG)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-6):
        return abs(self) < eps
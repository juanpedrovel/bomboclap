from decimal import Decimal, getcontext
from copy import deepcopy
from vector import Vector
from plane import Plane
from hyperplane import Hyperplane

getcontext().prec = 30


class LinearSystem:

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def swap_rows(self, row1, row2):
        self[row1], self[row2] = self[row2], self[row1]


    def multiply_coefficient_and_row(self, coefficient, row):

        nv = self[row].normal_vector
        k = self[row].constant_term
        new_nv = nv.times_scalar(coefficient)
        new_consant_term = k * coefficient
        self[row] = Plane(new_nv, new_consant_term)


    def add_multiple_times_row_to_row(self, coefficient, row_to_add, 
                                      row_to_be_added_to):
        nv1 = self[row_to_add].normal_vector
        nv2 = self[row_to_be_added_to].normal_vector
        k1 = self[row_to_add].constant_term
        k2 = self[row_to_be_added_to].constant_term

        new_nv = nv1.times_scalar(coefficient).plus(nv2)
        new_k = k2 + (k1 * coefficient)

        self[row_to_be_added_to] = Plane(new_nv, new_k)


    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices

    def compute_triangular_form(self):
        system = deepcopy(self)

        variable = 0
        num_variables = system.dimension
        num_equations = len(system)
        
        for index, plane in enumerate(system):
            while variable < num_variables:
                coefficient = MyDecimal(plane.normal_vector[variable])
                if coefficient.is_near_zero():
                    if not system.swap_with_row_below_for_non_zero_coefficient(index, variable):
                        variable += 1
                        continue
                system.clear_coefficients_below(index, variable)
                variable += 1
                break               

        return system


    def swap_with_row_below_for_non_zero_coefficient(self, index, variable):
        num_equations = len(self)
        
        for new_row in range(index+1, num_equations):
            if not MyDecimal(self[new_row].normal_vector[variable]).is_near_zero():
                self.swap_rows(index, new_row)
                return True
        return False


    def clear_coefficients_below(self, i, variable):
        num_equations = len(self)
        beta = self[i].normal_vector[variable]

        for row in range(i + 1, num_equations):
            if MyDecimal(self[row].normal_vector[variable]).is_near_zero():
                continue
            #factor is the number to multiply row i to cancel variable in new row
            factor =  - self[row].normal_vector[variable] / beta
            self.add_multiple_times_row_to_row(factor, i, row)


    def compute_rref(self):
        tf = self.compute_triangular_form()

        num_equations = len(tf)
        first_non_zero_indexes = tf.indices_of_first_nonzero_terms_in_each_row()

        for row in range(num_equations - 1, -1, -1):
            j = first_non_zero_indexes[row]
            if j == -1:
                continue   
            tf.scale_row_to_make_coefficient_one(row, j)
            tf.clear_coefficients_above(row, j)

        return tf


    def scale_row_to_make_coefficient_one(self, row, j):
        j_coefficient = self[row].normal_vector[j]
        factor = Decimal('1') / j_coefficient
        self.multiply_coefficient_and_row(factor, row)


    def clear_coefficients_above(self, i, variable):
        for row in range(i-1, -1, -1):
            if MyDecimal(self[row].normal_vector[variable]).is_near_zero():
                continue
            #factor is the number to multiply row i to cancel variable in new row
            factor =  - self[row].normal_vector[variable]
            self.add_multiple_times_row_to_row(factor, i, row)


    def gaussian_solution(self):
        rref = self.compute_rref()
        
        num_equations = len(rref)
        num_variables = rref.dimension

        rref.check_if_no_solution()
        rref.check_if_infinite_solutions()

        solution = [rref.planes[i].constant_term for 
                    i in range(num_variables)]
        return Vector(solution)


    def check_if_no_solution(self):
        first_non_zero_indexes = self.indices_of_first_nonzero_terms_in_each_row()
        for i in range(len(first_non_zero_indexes)):
            if first_non_zero_indexes[i] == -1:
                if not MyDecimal(self[i].constant_term).is_near_zero():
                    raise Exception(NO_SOLUTIONS_MSG)
        return


    def check_if_infinite_solutions(self):
        num_variables = self.dimension
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        number_of_pivots = 0
        for i in pivot_indices:
            if i != -1:
                number_of_pivots += 1
        if number_of_pivots < num_variables:
            raise Exception(INF_SOLUTIONS_MSG)
        return

    def parametrization_solution(self):
        rref = self.compute_rref()

        rref.check_if_no_solution()
            
        direction_vectors = rref.extract_direction_vectors()
        basepoint = rref.extract_basepoint()

        return Parametrization(basepoint, direction_vectors)

    def extract_direction_vectors(self):
        num_variables = self.dimension
        first_non_zero_indices = self.indices_of_first_nonzero_terms_in_each_row()
        free_variable_indices = set(range(num_variables)) - set(first_non_zero_indices)

        direction_vectors = []
        for free_var in free_variable_indices:
            vector_coords = [0] * num_variables
            vector_coords[free_var] = 1
            for i, p in enumerate(self.planes):
                pivot_var = first_non_zero_indices[i]
                if pivot_var == -1:
                    break
                vector_coords[pivot_var] = - p.normal_vector[free_var]
            direction_vectors.append(Vector(vector_coords))

        return direction_vectors

    def extract_basepoint(self):
        num_variables = self.dimension
        first_non_zero_indices = self.indices_of_first_nonzero_terms_in_each_row()

        basepoint_coords = [0] * num_variables

        for i, p in enumerate(self.planes):
            pivot_var = first_non_zero_indices[i]
            if pivot_var == -1:
                break
            basepoint_coords[pivot_var] = p.constant_term
        
        return Vector(basepoint_coords)



    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]


    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):

    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps


class Parametrization:

    def __init__(self, basepoint, direction_vectors):
        
        self.basepoint = basepoint
        self.direction_vectors = direction_vectors
        self.dimension = self.basepoint.dimension

        try:
            for v in direction_vectors:
                assert v.dimension == self.dimension
        except AssertionError:
            raise Exception('Basepoint and vectors should live in same dimension')

    def __str__(self):

        output = ''
        for coord in range(self.dimension):
            output += 'x_{} = {} '.format(coord + 1,
                                          round(self.basepoint[coord], 3))
            for free_var, vector in enumerate(self.direction_vectors):
                output += '+ {} t_{}'.format(round(vector[coord], 3),
                                             free_var + 1)
            output += '\n'
        return output



p0 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
p1 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')

s = LinearSystem([p0,p1,p2,p3])

print(s.indices_of_first_nonzero_terms_in_each_row())
print('{}, {}, {}, {}'.format(s[0],s[1],s[2],s[3]))
print(len(s))
print(s)

s[0] = p1
print(s)

print(MyDecimal('1e-9').is_near_zero())
print(MyDecimal('1e-11').is_near_zero())
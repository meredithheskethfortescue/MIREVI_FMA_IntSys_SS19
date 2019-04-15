import timeit
import numpy as np

repetitions = 20

# C-style arrays are faster on row-operations (axis 0)
# because the memory is allocated row-wise
array_c = np.ones((10000, 10000), dtype=np.uint16)
t_numpy_axis0 = timeit.timeit(lambda: array_c.sum(axis=0), number=repetitions) / repetitions
t_numpy_axis1 = timeit.timeit(lambda: array_c.sum(axis=1), number=repetitions) / repetitions
print("numpy axis 0", t_numpy_axis0)
print("numpy axis 1", t_numpy_axis1)

# Fortran-style arrays are faster on column-operations (axis 1)
# because the memory is allocated column-wise
array_fortran = np.asfortranarray(array_c)
t_fortran_axis0 = timeit.timeit(lambda: array_fortran.sum(axis=0), number=repetitions) / repetitions
t_fortran_axis1 = timeit.timeit(lambda: array_fortran.sum(axis=1), number=repetitions) / repetitions
print("fortran axis 0", t_fortran_axis0)
print("fortran axis 1", t_fortran_axis1)

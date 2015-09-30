# Example of compiling code with cython

cpdef int do_work_fastest(int num_simulations=10**6):
    cdef int x = 0
    cdef int i
    with nogil:
        for i in range(num_simulations):
            x += 1
        return x
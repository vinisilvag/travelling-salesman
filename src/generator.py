import numpy as np
from random import randint

def main():
    for idx in range(100):
        exp = randint(4, 10)
        size = pow(2, exp)

        entrie = np.random.randint(1, np.iinfo('uint8').max + 1, size=(size, size), dtype=np.int32)

        di = np.diag_indices(size)
        entrie[di] = -1

        # write entrie in experiments/instances
        print(entrie)

        return entrie

if __name__ == "__main__":
    main()

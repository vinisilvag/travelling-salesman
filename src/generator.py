import numpy as np
from random import randint

def generate():
    for idx in range(10):
        exp = randint(4, 10)
        size = pow(2, exp)

        entrie = np.random.randint(1, np.iinfo('uint8').max + 1,
                                   size=(size, size),
                                   dtype=np.int32)

        di = np.diag_indices(size)
        entrie[di] = -1

        with open(f'../experiments/instances/entrie{idx}.txt', 'w') as file:
            np.savetxt(file, entrie, fmt='%s')

        print(f'Instance {idx} created')

def main():
    generate()

if __name__ == "__main__":
    main()

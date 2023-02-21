import numpy as np
import random
class Random:
    def main():
        x_axis=np.random.randint(10,90,12)
        y_axis=np.random.randint(10,90,12)
        # x_axis=np.array_split(x_axis, 1)
        # y_axis=np.array_split(y_axis, 1)
        print(x_axis)
        print(y_axis)
        print(len(x_axis))
        print(len(y_axis))
Random.main()
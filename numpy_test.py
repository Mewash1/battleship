import numpy as np

square_width = 13
grid_width = 3
a = np.zeros((grid_width, grid_width))
print(a)
ix = 0
iy = 0
i_width = 0
i_column = 0
with np.nditer(a, op_flags=['readwrite']) as it:
    for x in it:
        x[...] = (ix, iy)
        ix += square_width
        i_width += 1
        if i_width == grid_width:
            i_column += 1
            i_width = 0
            ix = 0
            iy += square_width



print(a)

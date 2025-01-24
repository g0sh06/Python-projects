import matplotlib.pyplot as plt
import numpy as np

width, height = 800, 800
xmin, xmax = -4, 4
ymin, ymax = -4, 4
max_iter = 100

# in the mandelbrot method we declare the Mandelbrot algorithms
# z(n+1) = z⌃2(n) + c
def mandelbrot(c, max_iter):
    z = 0
    # for all n variables intul it reaches the biggest iteration
    for n in range(max_iter):
        z = z**2 + c
        if z == 0:
            return 0
        elif abs(z) > 2:
            return z  # Return the number of iterations at divergence
    return max_iter

# for n in range(10):
#     print(mandelbrot(1, 100000000))

# we generate the mandelbrot set by iterating over each pixel in the specified grid
# and compute the Mandelbrot set value(from mandelbrot function) for each point
def mandelbrot_generate(width, height, xmin, xmax, ymin, ymax, max_iter):
    mandelbrot_set = np.zeros((width, height), dtype=float)
    # realNumber and imaginaryNumber represent the the consecutive real parts(x-values, y-values
    # of complex numbers in the grid.
    # we are using the following formula:
    # imaginaryNumber = (ymax - ymin) / (height - 1)
    # it ensures that every pixel of the grid corresponds to unique part of the complex number
    realNumber = (xmax - xmin) / (width - 1)
    imaginaryNumber = (ymax - ymin) / (height - 1)

    for n in range(width):
        for i in range(height):
            # calculate the real an real and imaginary parts based on the pixel's position in the grid
            real = float(xmin + n * realNumber)
            imag = float(ymin + i * imaginaryNumber)
            # c is the complex number from the real one and the imaginary one
            c = complex(real, imag)
            mandelbrot_set[n, i] = mandelbrot(c, max_iter)
    return mandelbrot_set

# in display_mandelbrot method we parse all of data in the mandebrot_set array and
# create a statistical-like visualization using matplotlib and .imshow method
def display_mandelbrot(mandelbrot_set, xmin, xmax, ymin, ymax):
    plt.imshow(mandelbrot_set.T, extent=(xmin, xmax, ymin, ymax), cmap='inferno')
    plt.title('Mandelbrot set')
    plt.xlabel('Real numbers')
    plt.ylabel('Imaginary numbers')
    plt.show()


mandelbrot_set = mandelbrot_generate(width, height, xmin, xmax, ymin, ymax, max_iter)
display_mandelbrot(mandelbrot_set, xmin, xmax, ymin, ymax)







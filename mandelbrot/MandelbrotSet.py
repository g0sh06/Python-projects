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
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2])

def plot_mandelbrot(xmin=-2, xmax=1, ymin=-1.5, ymax=1.5, width=800, height=800, max_iter=100, cmap='hot'):
    mandelbrot_set = generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)
    plt.imshow(mandelbrot_set, extent=(xmin, xmax, ymin, ymax), cmap=cmap)
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.title("Mandelbrot Set")
    plt.show()

if __name__ == '__main__':
    x_center = float(input("Enter x center: "))
    y_center = float(input("Enter y center: "))
    zoom = float(input("Enter zoom level (e.g. 2 = zoom in 2x): "))
    scale = 1.5 / zoom
    plot_mandelbrot(xmin=x_center - scale, xmax=x_center + scale,
                    ymin=y_center - scale, ymax=y_center + scale)










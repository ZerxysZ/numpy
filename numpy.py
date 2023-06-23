import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_set(width, height, zoom, max_iter):
    x = np.linspace(-2.5/zoom, 1/zoom, width)
    y = np.linspace(-1/zoom, 1/zoom, height)
    c = x[:, np.newaxis] + 1j * y[np.newaxis, :]
    z = np.zeros_like(c)
    img = np.zeros((height, width))

    for i in range(max_iter):
        mask = np.abs(z) < 10
        z[mask] = z[mask] * z[mask] + c[mask]
        img += np.abs(mask.astype(int))

    return img

# Generate the Mandelbrot set
width = 800
height = 600
zoom = 200
max_iter = 1000

mandelbrot_img = mandelbrot_set(width, height, zoom, max_iter)

# Display the Mandelbrot set
plt.figure(figsize=(10, 8))
plt.imshow(mandelbrot_img, cmap='hot', extent=(-2.5, 1, -1, 1))
plt.colorbar(label='Iterations')
plt.title('Mandelbrot Set')
plt.xlabel('Re')
plt.ylabel('Im')
plt.show()

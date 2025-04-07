import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def eksplisitt_euler(h, k, tmax):

    t0 = 0
    tn = tmax
    x0 = 0
    xn = np.pi

    x = np.arange(x0, xn + h, h)
    t = np.arange(t0, tn + k, k)
    Nx, Nt = len(x), len(t)

    u = np.zeros((Nx, Nt))
    u[:, 0] = np.sin(x)

    for j in range(0, Nt - 1):
        for i in range(1, Nx - 1):
            u[i, j+1] = u[i, j] + (k/ h**2) * (u[i+1, j] - 2 * u[i, j] + u[i-1, j])

    return x, t, u

def animertLosning(h, k, tmax):
    x, t, u = eksplisitt_euler(h, k, tmax)

    fig, ax = plt.subplots()
    line, = ax.plot(x, u[:, 0], label="Varmeutvikling")
    ax.set_ylim(-1, 1)
    ax.set_xlabel("x")
    ax.set_ylabel("u(x,t)")
    ax.legend()

    def update(frame):
        line.set_ydata(u[:, frame])
        return line,

    ani = animation.FuncAnimation(fig, update, frames=u.shape[1], interval=50)
    plt.show()


h = 0.1
k = 0.001
tmax = 1

animertLosning(h, k, tmax)
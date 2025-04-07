import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.linalg import solve_banded

def implisitt_euler(h, k, tmax):

    t0 = 0
    tn = tmax
    x0 = 0
    xn = np.pi

    x = np.arange(x0, xn + h, h)
    t = np.arange(t0, tn + k, k)
    Nx, Nt = len(x), len(t)

    u = np.zeros((Nx, Nt))
    u[:, 0] = np.sin(x)

    A = np.zeros((3, Nx - 2))
    A[0, 1:] = - (k / h**2) * np.ones(Nx - 3)
    A[1, :] = (1 + 2 * (k / h**2)) * np.ones(Nx - 2)
    A[2, :-1] = - (k / h**2) * np.ones(Nx - 3)

    for j in range(0, Nt - 1):
        u_j = u[1:-1, j]

        u[1:-1, j+1] = solve_banded((1,1), A, u_j)

    return x, t, u

def animertLosning(h, k, tmax):
    x, t, u = implisitt_euler(h, k, tmax)

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
k = 0.1
tmax = 10

animertLosning(h, k, tmax)
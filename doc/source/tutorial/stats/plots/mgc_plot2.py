import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multiscale_graphcorr


def sim_plot(x, y, sim_name):
    """Plot simulations."""
    fig = plt.figure(figsize=(8,8))
    fig.suptitle(sim_name + " Simulation", fontsize=17)
    plt.scatter(x, y)
    plt.show()


x = np.array([-0.915363905, 2.134736725, 1.591825890, -0.947720469,
              -0.629203447, 0.157367412, -3.009624669, 0.342083914,
              0.126834696, 2.009228424, 0.137638139, -4.168139174,
              1.854371040, 1.696600346, -2.454855196, 1.770009913,
              -0.080973938, 1.985722698, 0.671279564, 1.521294941])
y = np.array([0.12441532, -2.63498763, 2.18349959, -0.58779997,
              -1.58602656, 0.35894756, -0.73954299, 1.76585591,
              -0.35002851, 0.48618590, 0.95628300, 1.99038991,
              1.92277498, 1.34861841, 1.42509605, 0.65982368,
              -1.56731299, -0.17000082, 1.81187432, -0.73726241])


sim_plot(x, y, "Spiral")

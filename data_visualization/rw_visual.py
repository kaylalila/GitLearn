import matplotlib.pyplot as plt
from random_walk import RandomWalk

while(True):
    rw = RandomWalk()
    rw.fill_work()

    point_number = list(range(rw.num_points))
    plt.scatter(rw.x_value, rw.y_value, c = point_number, s = 10,
                                        cmap=plt.cm.Blues, edgecolors='none')

    plt.scatter(0, 0, c = 'green', edgecolors='none', s=50)
    plt.scatter(rw.x_value[-1], rw.y_value[-1], c = 'red', edgecolors='none', s=50) 

    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another random walk (y/n): ")
    if (keep_running == 'n'):
        break


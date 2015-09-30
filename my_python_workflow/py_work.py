# In packages, we put our complex code. It acts as a storage space.

def do_work_in_pycharm(num_simulations=10**6):
    x = 0
    for i in range(num_simulations):
        x += 1
    return x
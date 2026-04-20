import pandas as pd
import numpy as np
np.random.seed(0)

def Get_Arrival():
    return np.random.exponential(scale=1/3)

def Get_Service():
    return np.random.exponential(scale=1/4)

def main():
    next_arrival = Get_Arrival()
    next_depart = np.inf
    utilization = 0
    queue = 0
    queue_time = 0
    sys_time = 0
    time = 0
    max_time = 500
    while time <= max_time:
        prev_time = time
        prev_queue = queue
        prev_utilization = utilization
        if next_arrival < next_depart:
            time = next_arrival
            if utilization == 0:
                utilization = 1
                next_depart = time + Get_Service()
            else:
                queue += 1
            next_arrival = time + Get_Arrival()
        else: # Depart < Arrival
            time = next_depart
            if queue >= 1:
                queue -= 1
                next_depart = time + Get_Service()
            else:
                utilization = 0
                next_depart = np.inf
        if prev_queue > 0:
            queue_time += queue * (time - prev_time)
        if prev_utilization == 1:
            sys_time += (time - prev_time) * (prev_queue + prev_utilization)
        util_unit = prev_utilization * (time - prev_time)

    avg_queue_time = queue_time / max_time
    avg_sys_time = sys_time / max_time
    avg_queue_length = queue/max_time
    avg_sys_length = sys_time/max_time
    avg_utilization = util_unit / max_time



if __name__ == "__main__":
    main()
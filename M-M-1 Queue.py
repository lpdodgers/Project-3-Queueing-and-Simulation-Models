from cmath import inf
import pandas as pd
import numpy as np

def Get_Arrival():

    return None

def Get_Service():
    np.random.exponential(scale=1)
    return None

def main():
    next_arrival = Get_Arrival()
    next_depart = inf
    utilization = 0
    queue = 0
    queue_time = 0
    sys_time = 0
    time = 0
    max_time = 500
    while time <= 500:
        if next_arrival < next_depart:
            time = next_arrival
            if utilization == 0:
                utilization = 1
                next_depart = Get_Service()
            else:
                queue += 1
            next_arrival = Get_Arrival()
            #Update Q_Time & Sys_Time
        else:
            time = next_arrival
            if queue >= 1:
                queue -= 1
                next_depart = Get_Service()
            else:
                utilization = 0
                next_depart = inf
                #Update Q_Time & System_Time


if __name__ == "__main__":
    main()
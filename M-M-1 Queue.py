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
    arrivals = 0
    departions = 0
    while time <= max_time:
        arrivals += 1
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
            departions += 1
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

    avg_queue_length = queue_time / max_time
    avg_utilization = sys_time / max_time
    avg_sys_length = avg_queue_length + avg_utilization
    avg_queue_time =
    avg_sys_time =

    print(f'Average Queue Time: {avg_queue_time}')
    print(f'Average System Time: {avg_sys_time}')
    print(f'Average Queue Length: {avg_queue_length}')
    print(f'Average System Length: {avg_sys_length}')
    print(f'Average Utilization: {avg_utilization}')


if __name__ == "__main__":
    main()
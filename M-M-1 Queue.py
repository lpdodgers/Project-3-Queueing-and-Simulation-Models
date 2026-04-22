import numpy as np
import scipy.stats as sc

def Get_Arrival():
    return np.random.exponential(scale=1/3)

def Get_Service():
    return np.random.exponential(scale=1/4)

def running():
    next_arrival = Get_Arrival()
    next_depart = np.inf
    utilization = 0
    queue = 0
    queue_time = 0
    sys_time = 0
    time = 0
    max_time = 500
    arrivals = 0
    departures = 0
    util_time = 0
    while time <= max_time:
        prev_time = time
        prev_queue = queue
        prev_utilization = utilization
        if next_arrival < next_depart:
            arrivals += 1
            time = next_arrival
            if utilization == 0:
                utilization = 1
                next_depart = time + Get_Service()
            else:
                queue += 1
            next_arrival = time + Get_Arrival()
        else: # Depart < Arrival
            departures += 1
            time = next_depart
            if queue >= 1:
                queue -= 1
                next_depart = time + Get_Service()
            else:
                utilization = 0
                next_depart = np.inf
        queue_time += prev_queue * (time - prev_time)
        sys_time += (time - prev_time) * (prev_queue + prev_utilization)
        util_time += (time - prev_time) * prev_utilization

    # queue_time = queue * time => (queue * time) / time = queue
    avg_queue_length = queue_time / max_time
    avg_utilization = util_time / max_time
    avg_sys_length = sys_time / max_time
    # Using Little's Law
    lamb = arrivals / max_time
    avg_queue_time = avg_queue_length / lamb
    avg_sys_time = avg_sys_length / lamb

    #print(f'Average Queue Time: {avg_queue_time}')
    #print(f'Average System Time: {avg_sys_time}')
    #print(f'Average Queue Length: {avg_queue_length}')
    #print(f'Average System Length: {avg_sys_length}')
    #print(f'Average Utilization: {avg_utilization}')
    return avg_queue_time, avg_sys_time, avg_queue_length, avg_sys_length, avg_utilization

def CI(dat):
    n = len(dat)
    sample_mean = np.mean(dat)
    sample_std = np.std(dat, ddof = 1)
    t_value = sc.t.ppf(.975, df = n-1)
    margin_of_error = t_value * (sample_std / np.sqrt(n))
    ci = float(sample_mean - margin_of_error), float(sample_mean + margin_of_error)
    return ci

def main():
        n = int(input(f'Number of Replications: '))
        results = []
        for _ in range(int(n)):
            results.append(running())
        results = np.array(results)
        outputs = results.mean(axis=0)

        #Confidence Intervals | alpha = .05 | see CI

        #Print
        print(f'Average Queue Time: {outputs[0]}, CI: {CI(results[:,0])}')
        print(f'Average System Time: {outputs[1]}, CI: {CI(results[:, 1])}')
        print(f'Average Queue Length: {outputs[2]}, CI: {CI(results[:, 2])}')
        print(f'Average System Length: {outputs[3]}, CI: {CI(results[:, 3])}')
        print(f'Average Utilization: {outputs[4]}, CI: {CI(results[:, 4])}')


if __name__ == "__main__":
    main()
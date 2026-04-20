from cmath import inf
import pandas as pd

def Get_Arrival():
    pass

def Get_Service():
    pass

def main():
    Next_Arrival = Get_Arrival()
    Next_Depart = inf
    Utilization = 0
    Queue = 0
    Queue_Time = 0
    Sys_Time = 0
    Time = 0

def idk():
    while Time <= 0:
        if Next_Arrival < Next_Depart:
            Time = Next_Arrival
            if utilization == 0:
                utilization = 1
                Next_Depart = Get_Service()
            else:
                queue += 1
            Next_Arrival = Get_Arrival()
            #Update Q_Time & Sys_Time
        else:
            Time = Next_Arrival
            if queue >= 1:
                queue -= 1
                Next_Depart = Get_Service()
            else:
                utilization = 0
                Next_Depart = inf
                #Update Q_Time & System_Time


if __name__ == "__main__":
    main()
import json
import os
import polars as pl
import datetime 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

Days_Before = 5

# Open and read the JSON file
def file_list(json_file):
    # Read the JSON file
    with open(json_file, "r") as file:
        data = json.load(file)
    start_date_str = data["availability_window"]["start"]
    end_date_str = data["availability_window"]["end"]
    
    start_date = datetime.strptime(start_date_str.replace("Z", ""), "%Y-%m-%dT%H:%M:%S")
    end_date = datetime.strptime(end_date_str.replace("Z", ""), "%Y-%m-%dT%H:%M:%S")
    
    files = []

    # Loop from start to end date
    current_date = start_date - timedelta(days=Days_Before)
    while current_date.date() <= end_date.date():
        # Construct path like data/2025/12/10.csv
        file_path = os.path.join(
            "data",     # replace with name of file
            str(current_date.year),
            f"{current_date.month:02d}",
            f"{current_date.day:02d}.csv"
        )
        files.append(file_path)
        current_date += timedelta(days=1)
        
    return files

#-------------------------------------------------------------------------------------

def Event_Dur(json_file):
    # Read the JSON file
    with open(json_file, "r") as file:
        data = json.load(file)

    duration_days = data["event_duration"].get("days", 0)
    duration_hours = data["event_duration"].get("hours", 0)
    duration_minutes = data["event_duration"].get("minutes", 0)
    duration_seconds = data["event_duration"].get("seconds", 0)
    time_delta_duration = timedelta(days = duration_days,
    hours = duration_hours,
    minutes = duration_minutes,
    seconds = duration_seconds
    )


    return time_delta_duration

#---------------------------------------------------------------------------------------------------------------

Event_Length = Event_Dur(json_file)

target_score = {}

Weight_Vector = [1,1,1]

targets = [] 

iterating_time = 1  

Min_Length_Per_Day = #input-----

Local_wdt_start = #input
Local_wdt_end = #input

#-----------------------------------------------------------------------------------------------------------------

    
    def find_score(data,city0,city1,arrive_before_time,meeting_end):
    
        # 1. Calculate the arrival time for all flights # and filter out flights that don't match our criteria. 
        best_dept_flight = data.with_columns((pl.col("SCHEDULED_DEPARTURE_DATE_TIME_LOCAL") + pl.col("FLIGHT_DURATION")).alias("SCHEDULED_ARRIVAL_DATE_TIME_LOCAL")).filter((pl.col("DEPCITY") == city0) & (pl.col("ARRCITY") == city1) & (pl.col("SCHEDULED_ARRIVAL_DATE_TIME_LOCAL") < arrive_before_time)).sort("SCHEDULED_DEPARTURE_DATE_TIME_LOCAL", descending=True ).head(1) # 3. Select the top one return best_flight
        #relevant_data = data.filter((pl.col("DEPCITY") == city0) & (pl.col("ARRCITY")) == city1)& (arrive_before_time >pl.col('SCHEDULED_ARRIVAL_DATE_TIME_LOCAL'))
        
       # return best_dept_flight['SCHEDULED_DEPARTURE_DATE_TIME_LOCAL','ESTIMATED_CO2_TOTAL_TONNES']
    
    
    
    
    #def arrival_time(data,city0,city1,meeting_end):
    
        # 1. Calculate the departure time for all flights # and filter out flights that don't match our criteria. 
        best_arv_flight = data.with_columns((pl.col("SCHEDULED_DEPARTURE_DATE_TIME_LOCAL") + pl.col("FLIGHT_DURATION")).alias("SCHEDULED_ARRIVAL_DATE_TIME_LOCAL")).filter((pl.col("DEPCITY") == city0) & (pl.col("ARRCITY") == city1) & (pl.col("SCHEDULED_DEPARTURE_DATE_TIME_LOCAL") > meeting_end)).sort("SCHEDULED_ARRIVAL_DATE_TIME_LOCAL", descending=False).head(1) # 3. Select the top one return best_flight
        #relevant_data = data.filter((pl.col("DEPCITY") == city0) & (pl.col("ARRCITY")) == city1)& (arrive_before_time >pl.col('SCHEDULED_ARRIVAL_DATE_TIME_LOCAL'))
        
        #return best_arv_flight['SCHEDULED_ARRIVAL_DATE_TIME_LOCAL','ESTIMATED_CO2_TOTAL_TONNES']
    
    
    #def difference():
        dep_optimal = best_dept_flight['SCHEDULED_DEPARTURE_DATE_TIME_LOCAL','ESTIMATED_CO2_TOTAL_TONNES']#departure_time(data,city0,city1,arrive_before_time)
        arr_optimal = best_arv_flight['SCHEDULED_ARRIVAL_DATE_TIME_LOCAL','ESTIMATED_CO2_TOTAL_TONNES']#arrival_time(data,city0,city1,meeting_end)
        difference = dep_optimal['SCHEDULED_DEPARTURE_DATE_TIME_LOCAL'][0] - arrival_time['SCHEDULED_ARRIVAL_DATE_TIME_LOCAL'][0]
        #return difference
    velctor = [difference,dep_optimal[1]+arr_optimal[1]]
    return vector
def find_score(dep,arr) :  #---------------------ankith code, 
    emission = 0          #####    inport data   ##### yerlan code
    time = 0              #####    inport data   ##### yerlan code
    return [emission, time]






#-----------------------------------------------------------------------------------------------------------------

def Make_DT(T, DT) :
    return datetime.combine(dateTimeInput.date(), timeInput.time())
    
def End(start_time) :
    nightlength = (Make_DT(UTC_wdt_start, start_time) - Make_DT(UTC_wdt_end, start_time)) + timedelta(days=1) +
    daylength = Make_DT(UTC_wdt_end, start_time) - Make_DT(UTC_wdt_start, start_time)
    nights = (Event_Length//daylength)
    return start_time + Event_Length + (nightlength * nights)

#-----------------------------------------------------------------------------------------------------------------
#------------------ITERATIONS----------------
#------------------ITERATE IN CITIES----------------

for target in targets :   #something to do with if dep and arr being the same gives time and emission as zero
    
    UTC_wdt_start = UTC - LOCAL + Local_wdt_start
    UTC_wdt_end = UTC - LOCAL + Local_wdt_end
    
    #initial start and end
    Start_Time = start_date   
    End_Time = End(Start_Time)
    
    Start_Times = []
    End_Times = []
    
    def Make_DT(T, DT) :
        return datetime.combine(dateTimeInput.date(), timeInput.time())
    
    def End(start_time) :
        nightlength = (Make_DT(UTC_wdt_start, start_time) - Make_DT(UTC_wdt_end, start_time)) + timedelta(days=1) +
        daylength = Make_DT(UTC_wdt_end, start_time) - Make_DT(UTC_wdt_start, start_time)
        nights = (Event_Length//daylength)
        return start_time + Event_Length + (nightlength * nights)

#------------------ITERATE IN RANGE OF POSIBLE MEETING TIME----------------

    while End_Time <= end_date :
        good = true
        if End_Time < UTC_wdt_start + Min_Length_Per_Day :  
            good = false
        if Start_Time + Min_Length_Per_Day > Make_DT(UTC_wdt_end, Start_Time) or Start_Time < Make_DT(UTC_wdt_start, Start_Time) :
            good = false
        if good == true : #read iff start end time -> meeting time per day in range(min,max)
            #Start_Times.append(Start_Time)  
            #End_Times.append(Start_Time)

#------------------ITERATE WRT ATTENDEES----------------
            times = []
            emissions = []
            
            for j in attendees :
                emissions.append(find_score(j,target)[1])
                times.append(find_score(j,target)[0])
                emissions.append(find_score(j,target)[0])
                times.append(find_score(j,target)[1])
    
            T_emission = sum(emissions)
            A_time = sum(times)/(len(times))
            fairness = np.std(times)
    
            score = T_emission * Weight_Vector[0] + A_time * Weight_Vector[1] + fairness * Weight_Vector[2]

#---------------------------------------------------------------------
        Start_Time += iterating_time #iterate         #times
        End_Time = End(Start_Time)   #next end

    
   # target_score[target] = [score, time]   #value for specific time     

####    can now sort target_score  to get list of best to worse















####    can now sort target_score  to get list of best to worse
















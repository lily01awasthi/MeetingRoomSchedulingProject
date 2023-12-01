import pandas as pd
import numpy as np
from datetime import datetime
from datetime import date, timedelta


# returns start and end date and times for the randomly generated meeting hours
def generate_random_meeting_times(start_date, end_date, start_hour, end_hour, max_duration=3):
    # generate a random meeting day
    room = np.random.randint(0,10)
    random_day = np.random.randint(0, (end_date - start_date).days)
    meeting_date = start_date + timedelta(days=random_day)

    # calculate start and end hours for the meetings
    start_time = np.random.randint(start_hour, end_hour)
    end_time = start_time + np.random.randint(1, max_duration + 1)

    # datetime.min.time() is utilized for a consistent starting time to combine with a date
    start_datetime = datetime.combine(meeting_date, datetime.min.time()) + timedelta(hours=start_time)
    end_datetime = datetime.combine(meeting_date, datetime.min.time()) + timedelta(hours=end_time)

    # to ensure the meeting is within the working hours
    if end_datetime.time() > datetime(end_datetime.year, end_datetime.month, end_datetime.day, end_hour, 0).time():
        end_datetime = datetime(end_datetime.year, end_datetime.month, end_datetime.day, end_hour, 0)
    return room,start_datetime, end_datetime


# Detects overlapping meetings throughout the time frame of Start and End Times
def find_overlapping_meetings(meetings):
    # sort the dataframe
    meetings = meetings.sort_values(by='Start Time').reset_index(drop=True)

    overlapping_meetings = []
    # iterating through meetings
    for i in range(len(meetings) - 1):
        current_meeting = meetings.iloc[i]
        next_meeting = meetings.iloc[i + 1]

        if current_meeting["End time"] > next_meeting["Start Time"] and current_meeting["Room"]==next_meeting["Room"]:
            overlapping_meetings.append((i, i + 1))
            print(f"Overlapping occurred for room {current_meeting['Room']} :Meeting {i} at {current_meeting['Start Time']}:"
                  f"{current_meeting['End time']} and {i + 1} at {next_meeting['Start Time']}:{next_meeting['End time']}")


if __name__ == '__main__':
    no_of_meetings = 200
    # Meetings for the calendar year 2024
    Start_date = date(2024, 1, 1)
    End_date = date(2024, 12, 31)
    Start_hour = 8  # work starting time at 8AM
    End_hour = 18  # work ending time at 6PM

    data = [generate_random_meeting_times(Start_date, End_date, Start_hour, End_hour) for _ in range(no_of_meetings)]
    df_meetings = pd.DataFrame(data, columns=["Room","Start Time", "End time"])
    print(df_meetings)
    find_overlapping_meetings(df_meetings)

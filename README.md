# MeetingRoomScheduling
__Overview__

**The Meeting Room Scheduling Optimization Project is a Python-based tool designed to help organizations manage and optimize the use of their meeting rooms. By identifying overlapping meeting schedules, the tool aids in maximizing room utilization and reducing scheduling conflicts.<br>

**Features**
Meeting Schedule Generation: Generate synthetic meeting schedules with specified constraints (e.g., meeting duration, working hours).<br>
Overlap Detection: Identify overlapping meetings in the schedule.<br>
Optimization Suggestions: Outline recommendations for rescheduling to reduce overlaps.<br>

**Installation**
To run this project, you need Python installed on your system along with the pandas and NumPy libraries.<br>

**Steps**:
**Clone the Repository:**<br>
https://github.com/lily01awasthi/MeetingRoomSchedulingProject.git <br>
cd MeetingRoomSchedulingProject<br>
Install Required Libraries:
pip install pandas numpy

**Usage**
**The project is divided into two main funtions:**

generate_random_meeting_times (start_date, end_date, start_hour, end_hour, max_duration=3):
This script generates a DataFrame of random meeting times.<br>
Modify parameters such as the number of meetings, start/end dates, and working hours as needed.<br>

find_overlapping_meetings(meetings):<br>
This script takes the generated meeting schedule and identifies overlapping meetings.<br>
Overlapping meeting details (start and end times) are printed for review.<br>

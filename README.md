Appointment Monitoring Script
This Python script monitors available appointment times on the DoctorEto platform and automatically opens a web browser tab for each newly available appointment. It uses the DoctorEto API to check for available time slots and opens reservation links for new appointments.
Features

Real-time Monitoring: Continuously checks for available appointment slots at a specified interval.
Automatic Browser Opening: Opens a new browser tab for each newly available appointment.
Threaded Execution: Uses ThreadPoolExecutor for efficient handling of API requests and browser operations.
Error Handling: Includes basic error handling for API request failures.

Requirements

Python 3.x
Required Python packages:
requests
webbrowser
concurrent.futures (included in Python standard library)
datetime (included in Python standard library)
time (included in Python standard library)



Installation

Clone or download the script to your local machine.
Install the required packages:pip install requests


Ensure you have a valid consultation_id and start_date for the DoctorEto API.

Usage

Modify the consultation_id and start_date in the script to match your desired appointment parameters. For example:monitor_appointments(consultation_id="44867", start_date="2025-04-21")


Run the script:python script.py


The script will:
Check the DoctorEto API for available appointment times.
Open a new browser tab for each new appointment found.
Print status messages to the console, including timestamps and appointment IDs.
Continue monitoring until manually stopped (Ctrl+C).



Code Structure

check_appointments(consultation_id, start_date): Fetches available appointment times from the DoctorEto API for a given consultation ID and start date. Returns a list of available appointment IDs.
open_appointment_link(appointment_id): Opens a browser tab for a specific appointment ID using the DoctorEto reservation URL.
monitor_appointments(consultation_id, start_date): Continuously monitors for new appointments, opening links for new ones and avoiding duplicates.

Notes

The script uses a 1-second delay between API checks to avoid overwhelming the server. Adjust time.sleep(1) in the monitor_appointments function if needed.
A 0.5-second delay is added in open_appointment_link to prevent browser overload. Modify time.sleep(0.5) as needed.
Ensure a stable internet connection to avoid API request failures.
The script requires a valid consultation_id and start_date in the format YYYY-MM-DD.
Stop the script by pressing Ctrl+C in the terminal.

Example
To monitor appointments for consultation ID 44867 starting from April 21, 2025:
monitor_appointments(consultation_id="44867", start_date="2025-04-21")

Disclaimer

This script interacts with the DoctorEto API. Ensure compliance with their terms of service.
Excessive API requests may lead to rate-limiting or account restrictions.
Use responsibly and verify the API endpoint and parameters before running.

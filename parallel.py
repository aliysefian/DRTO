import datetime
import requests
import webbrowser
import time
from concurrent.futures import ThreadPoolExecutor

def check_appointments(consultation_id, start_date):
    url = "https://api.doctoreto.com/api/web/patient/v1/consultation-times/days"
    params = {
        "consultation_id": consultation_id,
        "start_date": start_date,
        "day_navigate": "1"
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        available_appointments = []
        for day in data['items']['days']:
            for time_slot in day['times']:
                if time_slot['status'] == 1:
                    available_appointments.append(time_slot['id'])
        return available_appointments
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

def open_appointment_link(appointment_id):
    appointment_url = f"https://doctoreto.com/reserve/consultation?item_type=0&item_id={appointment_id}"
    webbrowser.open_new_tab(appointment_url)  # Opens each link in a new tab
    print(f"Opened appointment ID {appointment_id} at {appointment_url}")
    time.sleep(1)  # Optional: Delay to avoid overwhelming the browser

def monitor_appointments(consultation_id="3022", start_date="2024-10-28"):
    opened_ids = set()
    with ThreadPoolExecutor() as executor:
        while True:
            future = executor.submit(check_appointments, consultation_id, start_date)
            available_appointments = future.result()
            
            for appointment_id in available_appointments:
                if appointment_id not in opened_ids:
                    opened_ids.add(appointment_id)
                    executor.submit(open_appointment_link, appointment_id)
                    print(f"{datetime.datetime.now()} - Appointment available. Opening link for ID {appointment_id}.")
                    
            if not available_appointments:
                print(f"{datetime.datetime.now()} - No available appointments yet.")
            time.sleep(1)

# Start monitoring appointments
monitor_appointments(consultation_id="44867", start_date="2025-06-28")
# monitor_appointments(consultation_id="3022", start_date="2025-04-13")
# monitor_appointments(consultation_id="3022", start_date="2025-06-28")


import datetime
import requests
import webbrowser
import time

def check_and_open_appointments(consultation_id="3022", start_date="2024-10-28"):
    # API URL with specified parameters
    url = "https://api.doctoreto.com/api/web/patient/v1/consultation-times/days"
    params = {
        "consultation_id": consultation_id,
        "start_date": start_date,
        "day_navigate": "1"
    }

    while True:
        # Make a GET request to the API
        response = requests.get(url, params=params)
        data = response.json()
        
        # Check if there are available times
        available_found = False
        for day in data['items']['days']:
            for time_slot in day['times']:
                if time_slot['status'] == 1:
                    # Construct the URL to open in Chrome with the extracted item ID
                    appointment_id = time_slot['id']
                    appointment_url = f"https://doctoreto.com/reserve/consultation?item_type=0&item_id={appointment_id}"
                    
                    # Open the URL in Chrome
                    webbrowser.open(appointment_url)
                    print(f"Opened appointment ID {appointment_id} at {appointment_url}")
                    available_found = True
                    break  # Exit loop when the first available appointment is found
            if available_found:
                print(str(datetime.datetime.now())+"no yet")
                break
        if len(data['items']['days'][0]['times'])==0:
            print(str(datetime.datetime.now())+"   :no open yet")
        # Wait for 1 second before checking again
        if not available_found:
            time.sleep(1)

# Start checking appointments with desired consultation_id and start_date
# check_and_open_appointments(consultation_id="44867", start_date="2024-10-28")
check_and_open_appointments(consultation_id="3022", start_date="2024-10-28")


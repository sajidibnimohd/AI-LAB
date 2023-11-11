class AppointmentScheduler:
    def __init__(self):
        self.appointments = {}  # Dictionary to store scheduled appointments

    def schedule_appointment(self, day, time):
        if day.lower() in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday'] and 9 <= time <= 17:
            if (day, time) not in self.appointments:
                self.appointments[(day, time)] = "Scheduled"
                return True, "Appointment scheduled successfully!"
            else:
                return False, "Appointment slot is already taken."
        else:
            return False, "Invalid day/time for appointment."

# Example usage
scheduler = AppointmentScheduler()
while True:
    # Take user input for day and time
    day = input("Enter the day for the appointment (Monday/Tuesday/Wednesday/Thursday/Friday): ")
    try:
        time = int(input("Enter the time for the appointment (9-17): "))
    except ValueError:
        print("Invalid input for time. Please enter a number between 9 and 17.")
        continue
    success, message = scheduler.schedule_appointment(day, time)
    print(message)
    # Ask the user if they want to schedule another appointment
    another_appointment = input("Do you want to schedule another appointment? (yes/no): ")
    if another_appointment.lower() != 'yes':
        break

# Print scheduled appointments
print("\nScheduled Appointments:")
for slot, status in scheduler.appointments.items():
    print(f"Day: {slot[0]}, Time: {slot[1]}: Status: {status}")

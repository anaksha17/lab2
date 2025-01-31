# Environment Class
class HospitalEnvironment:
    def __init__(self):
        # Define the hospital layout and initial state
        self.locations = {
            "Storage": {"Medicine A": 5, "Medicine B": 3},  # Medicine storage area
            "Room 101": {"Patient": "John", "Medicine Needed": "Medicine A"},
            "Room 202": {"Patient": "Alice", "Medicine Needed": "Medicine B"},
            "Nurse Station": {"Staff Available": True}
        }
        self.robot_location = "Storage"  # Robot starts at the storage area

    def move_robot(self, new_location):
        # Move the robot to a new location
        if new_location in self.locations:
            self.robot_location = new_location
            print(f"Robot moved to {new_location}.")
        else:
            print(f"Invalid location: {new_location}.")

    def pick_up_medicine(self, medicine):
        # Pick up medicine from the storage area
        if self.robot_location == "Storage":
            if self.locations["Storage"].get(medicine, 0) > 0:
                self.locations["Storage"][medicine] -= 1
                print(f"Picked up {medicine}.")
                return True
            else:
                print(f"{medicine} is out of stock.")
        else:
            print("Robot must be at the storage area to pick up medicine.")
        return False

    def deliver_medicine(self, room, medicine):
        # Deliver medicine to a patient's room
        if self.robot_location == room:
            if self.locations[room]["Medicine Needed"] == medicine:
                print(f"Delivered {medicine} to {room}.")
                self.locations[room]["Medicine Needed"] = None  # Medicine delivered
                return True
            else:
                print(f"{room} does not need {medicine}.")
        else:
            print(f"Robot must be at {room} to deliver medicine.")
        return False

    def alert_staff(self):
        # Alert staff at the nurse station
        if self.robot_location == "Nurse Station":
            if self.locations["Nurse Station"]["Staff Available"]:
                print("Alerted staff at the nurse station.")
            else:
                print("No staff available at the nurse station.")
        else:
            print("Robot must be at the nurse station to alert staff.")


# Agent Class
class DeliveryRobot:
    def __init__(self, environment):
        self.env = environment
        self.carried_medicine = None  # Medicine currently carried by the robot

    def perform_task(self):
        # Perform a sequence of tasks to deliver medicine
        print("\nStarting delivery task...")

        # Step 1: Move to storage and pick up Medicine A
        self.env.move_robot("Storage")
        if self.env.pick_up_medicine("Medicine A"):
            self.carried_medicine = "Medicine A"

        # Step 2: Move to Room 101 and deliver Medicine A
        self.env.move_robot("Room 101")
        if self.carried_medicine:
            self.env.deliver_medicine("Room 101", self.carried_medicine)
            self.carried_medicine = None  # Medicine delivered

        # Step 3: Move to storage and pick up Medicine B
        self.env.move_robot("Storage")
        if self.env.pick_up_medicine("Medicine B"):
            self.carried_medicine = "Medicine B"

        # Step 4: Move to Room 202 and deliver Medicine B
        self.env.move_robot("Room 202")
        if self.carried_medicine:
            self.env.deliver_medicine("Room 202", self.carried_medicine)
            self.carried_medicine = None  # Medicine delivered

        # Step 5: Move to the nurse station and alert staff
        self.env.move_robot("Nurse Station")
        self.env.alert_staff()

        print("Delivery task completed.")


# Function to run the agent
def run_agent(agent):
    agent.perform_task()


# Create the hospital environment and robot
hospital = HospitalEnvironment()
robot = DeliveryRobot(hospital)

# Run the agent
run_agent(robot)

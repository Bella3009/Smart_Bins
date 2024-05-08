from pushbullet import Pushbullet
from datetime import datetime
from datetime import datetime

API_KEY = "o.eugg1BhvywYpKFvpbuG6MuX85gAqLBv0" # Key is changed to not save it publicaly

today = datetime.now()
day = today.weekday()
dayFile = str(day) + ".txt"
today = datetime.now()
day = today.weekday()
dayFile = str(day) + ".txt"

with open(dayFile,"r") as file:
    content = file.read()

pb = Pushbullet(API_KEY)
push = pb.push_note("Smart Bins Reminder", content)
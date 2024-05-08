from pushbullet import Pushbullet
from datetime import datetime

API_KEY = "o.eugg1BhvywYpKFvpbuG6MuX85gAqLBv0" # Key is changed to not save it publicaly

msg = ["Prepare the mixed garbage for tomorrow's collection.", "Prepare the organic garbage for tomorrow's collection.",
       "Prepare the recycling garbage for tomorrow's collection.","Prepare the organic garbage for tomorrow's collection.",
       "Prepare the mixed garbage for tomorrow's collection.", "Tomorrow there is no garbage to be collected.",
       "Prepare the organic garbage for tomorrow's collection."]

today = datetime.now()
day = today.weekday()

msgNotification = msg[day]

pb = Pushbullet(API_KEY)
push = pb.push_note("Smart Bins Reminder", msgNotification)
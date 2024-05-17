from pushbullet import Pushbullet
from datetime import datetime

API_KEY = "o.eugg1BhvywYpKFvpbuG6MuX85gAqLBv0"

# Message to send as notification in a list
msg = ["Prepare the mixed garbage for tomorrow's collection.", "Prepare the organic garbage for tomorrow's collection.",
       "Prepare the recycling garbage for tomorrow's collection.","Prepare the organic garbage for tomorrow's collection.",
       "Prepare the mixed garbage for tomorrow's collection.", "Tomorrow there is no garbage to be collected.",
       "Prepare the organic garbage for tomorrow's collection."]

today = datetime.now()
day = today.weekday() # result is a number from 0 (Monday) to 6 (Sunday)

msgNotification = msg[day]

pb = Pushbullet(API_KEY)
push = pb.push_note("Smart Bins Reminder", msgNotification) # Send notification
from pushbullet import Pushbullet
from datetime import datetime

API_KEY = "o.6fv3JTsQ1Y2XPgr5XMWPcXLZueO93fc" # Key is changed to not save it publicaly

filePath = "NotificationText/"

today = datetime.now()
day = today.weekday()
dayFile = filePath + str(day) + ".txt"

with open(dayFile,"r") as file:
    content = file.read()

pb = Pushbullet(API_KEY)
push = pb.push_note("Smart Bins Reminder", content)
filePath = "NotificationText/"

mon = filePath + "0.txt"
tue = filePath + "1.txt"
wed = filePath + "2.txt"
thu = filePath + "3.txt"
fri = filePath + "4.txt"
sat = filePath + "5.txt"
sun = filePath + "6.txt"

with open(mon,"r") as file:
    content = file.read()

print(content)
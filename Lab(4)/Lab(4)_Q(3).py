print "Days are numbered from saturday = 0 ... to friday = 6"

today = input("Enter today's day number: ")
future = input("Enter the number's of day after today: ")

di = {0: "Saturday", 1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday"}

if not future <= 7:
    future = future % 7

if future + today >= 7:
    future_today = (future + today) % 7
else:
    future_today = future + today

print "Today is ", di[today], " and the future day is ", di[future_today]

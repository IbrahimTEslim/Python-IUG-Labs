TotalSec = input("Enter time in seconds: ")

hours = TotalSec // 3600
TotalSec = TotalSec - (hours * 3600)

minutes = TotalSec // 60
TotalSec = TotalSec - (minutes * 60)

seconds = TotalSec

print "\nIt's equal to ", hours, ":", minutes, ":", seconds


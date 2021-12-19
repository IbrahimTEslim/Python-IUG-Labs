name =raw_input("Enter Employee Name: ")
hour=input("Enter N.O. Hours worked in a week: ")
hourperrate=input("Enter Hourly per rate: ")
taxrate=input("Enter Municipality tax rate %: ")
TaxRate=input("Enter Country tax rate %: ")

hour *=1.00 ;   hourperrate *=1.00;     taxrate*=1.00;  TaxRate*=1.00

di={"Name":name,"Hours":hour,"Pay":hourperrate,"texrate":taxrate,"TaxRate":TaxRate}

totalpay=di['Pay']*di['Hours']*1.00

print "\nEmployee Name: ",di['Name']
print "Hours Worked in week: ",di['Hours']
print "Hours rate: ",di['Pay']
print "Total PAy: ",di['Hours']*di['Pay']

print "\n-------------------------------\n"

print "Deducations:"

print "\tMunicipality tax (%",di['texrate'],"): ",totalpay*di['texrate']/100
print "\tCountry tax (%",di['TaxRate'],"): ",totalpay*di['TaxRate']/100

print"\tTotal Deducation: ",(totalpay*di['texrate']/100)+(totalpay*di['TaxRate']/100)

print "\nNet Pay: ",(totalpay-((totalpay*di['texrate']/100)+(totalpay*di['TaxRate']/100)))
import datetime

#datetime object
dt = datetime.datetime.now()

print("Datetime object =", dt)

# printing in dd/mm/YY H:M:S format using strftime()
dt_string = dt.strftime("Date: %d/%m/%Y  time: %H:%M:%S")
print("Current date and time =", dt_string) #
        

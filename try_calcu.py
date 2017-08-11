def try_function():
    try:
        hrs = float(raw_input("Enter Hours: "))
        rate = float(raw_input("Enter Rate: "))
        return hrs * rate
    except:
        print "Values are non numeric"
        quit()

pay = try_function()
print pay

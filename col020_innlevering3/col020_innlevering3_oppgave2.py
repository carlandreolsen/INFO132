while 1:
    from_location=input('Hvor i verden er du fra?')
    if from_location == "Norge" or from_location == "USA":
        break
    print("Har ikke hørt om den plassen. Har dessverre bare hørt om Norge og USA.")
while 1:
    where_location=input('Hvor i verden er du nå?')
    if where_location == "Norge" or where_location == "USA":
        break
    print("Har ikke hørt om den plassen. Har dessverre bare hørt om Norge og USA.")
while 1:    
    local_user_temperature=input('Hvor varmt blir det i morgen der du er?')
    try:
        local_user_temperature=float(local_user_temperature)
    except:
        print(local_user_temperature, " er ikke et tall.")
    if type(local_user_temperature) == type(0.1):
        if from_location == "Norge" and where_location == "Norge":
            print("Det blir ",local_user_temperature," grader Celcius i morgen.")
        if from_location != "Norge" and where_location == "Norge":
            print("Det blir ",local_user_temperature*1.8+32," grader Farenheit i morgen.")
        if from_location == "Norge" and where_location != "Norge":
            print("Det blir ",(local_user_temperature-32)/1.8," grader Celcius i morgen.")
        if from_location != "Norge" and where_location != "Norge":
            print("Det blir ",local_user_temperature," grader Farenheit i morgen.")     
        break

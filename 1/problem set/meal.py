def main():
    time = input("What time is it? ")
    time_float = convert(time)  # Get converted time
    
    # Now use time_float to check meals
    if 7.0 <= time_float <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_float <= 13.0:
        print("lunch time")
    elif 18.0 <= time_float <= 19.0:
        print("dinner time")

def convert(time):
    # Split "7:30" into hours and minutes
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return hours + minutes /60
    # Convert to float (7.5)
    # Return that float
    pass  # Replace with your code

if __name__ == "__main__":
    main()



#breakfast between 7 - 8
#lunch 12- 13
#dinner 18 19
#
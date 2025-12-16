import message as pwk

# Define recipient details and message
phone_number = "Your_Phone_Number"  # Ensure this includes a valid country code
message = "Hello World"

try:
    # Schedule message at least 2 minutes ahead of current time
    pwk.sendwhatmsg(phone_number, message, 24, 25)# Add time in 24hrs format: H, M
    print("Message scheduled successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
# This is a program which sends a Defined message to the Defined Phone Number, At a given time

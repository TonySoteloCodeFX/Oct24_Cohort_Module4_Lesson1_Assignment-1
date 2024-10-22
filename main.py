import mood_responses
import text_utils as u

print("-" * 50)
print("1. Python Modules and Data Handling Assignment\n")
print("How are you feeling today?")
print("Happy, Sad, or Mad")
mood = input("Enter Mood: ").lower()
print("")
print(mood_responses.mood_response(mood))
print("-" * 50)

print("2. Mastering Python Modules and Aliases\n")
s = "Hello, Welcome to the world of Python."
print(u.revers_string(s))
print("")
print(u.capitalize_string(s))
print("-" * 50)
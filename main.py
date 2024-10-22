import mood_responses

print("-" * 50)
print("How are you feeling today?")
print("Happy, Sad, or Mad")
mood = input("Enter Mood: ").lower()
print(mood_responses.mood_response(mood))
print("-" * 50)
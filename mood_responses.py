def mood_response(mood):
    match mood:
        case "happy":
            print("-" * 50)
            return "I'm glad you're having a great day!"
        case "sad":
            print("-" * 50)
            return "I hope your day gets better."
        case "mad":
            print("-" * 50)
            return "Count to 10 and take deep breaths. It will help."
        case _:
            print("-" * 50)
            return "That is not an option. Try again!"
        
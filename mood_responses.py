def mood_response(mood):
    match mood:
        case "happy":
            return "I'm glad you're having a great day!"
        case "sad":
            return "I hope your day gets better."
        case "mad":
            return "Count to 10 and take deep breaths. It will help."
        case _:
            return "That is not an option. Try again!"
        
import string

def check_strength_advanced(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Add numbers")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        suggestions.append("Add special characters")

    if score <= 2:
        return "Weak 🔴", score, suggestions
    elif score <= 4:
        return "Medium 🟡", score, suggestions
    else:
        return "Strong 🟢", score, suggestions
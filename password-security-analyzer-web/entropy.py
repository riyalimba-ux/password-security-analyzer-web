import math

def calculate_entropy(password):
    charset = 0

    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(not c.isalnum() for c in password):
        charset += 32

    if charset == 0:
        return 0

    return round(len(password) * math.log2(charset), 2)


def estimate_crack_time(password):
    charset = 0

    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(not c.isalnum() for c in password):
        charset += 32

    if charset == 0:
        return "Instant"

    guesses_per_sec = 1e9
    combinations = charset ** len(password)
    seconds = combinations / guesses_per_sec

    if seconds < 1:
        return "Instant"
    elif seconds < 60:
        return f"{round(seconds)} sec"
    elif seconds < 3600:
        return f"{round(seconds/60)} min"
    elif seconds < 86400:
        return f"{round(seconds/3600)} hr"
    elif seconds < 31536000:
        return f"{round(seconds/86400)} days"
    else:
        return f"{round(seconds/31536000)} years"
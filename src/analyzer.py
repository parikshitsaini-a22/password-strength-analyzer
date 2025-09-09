from zxcvbn import zxcvbn

def analyze_password(password: str):
    result = zxcvbn(password)
    score = result['score']
    feedback = result['feedback']
    return score, feedback

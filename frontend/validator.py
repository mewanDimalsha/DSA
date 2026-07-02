def is_valid_age(age):
    """Check if the provided age is a valid integer between 0 and 120."""
    if isinstance(age, str):
        try:
            age = int(age)

        except:
            return False
    elif isinstance(age, int) or isinstance(age, float):
        if age < 0 or age > 120:
            return False
    return True

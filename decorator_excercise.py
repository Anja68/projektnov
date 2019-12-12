

def restrict_access(func):
    def wrapper(*args, **kwargs):
        name = args[0]
        if name.startswith("A"):
            result = "Access denied"
        else:
            result = func(*args, **kwargs)
        return result
    return wrapper

@restrict_access
def treasurebox(username):
    return f"Granted Access to {username}"

def bank_safe(username):
    return f"Granted Access to rich bank safe to {username}"


if __name__ == '__main__':
    print(treasurebox("Anja"))
    print(bank_safe("Paul"))
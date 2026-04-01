def check_access(role):
    if role != "Doctor":
        raise PermissionError("Access Denied: Unauthorized Role.")
    print("Access Granted. Loading Patient Records...")

try:
    check_access("Nurse")
except PermissionError as e:
    print(f"Caught Error: {e}")
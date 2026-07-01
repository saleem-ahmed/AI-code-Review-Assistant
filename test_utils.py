from utils.validators import validate_file

print(validate_file("main.py", 1024))

print(validate_file("virus.exe", 1024))
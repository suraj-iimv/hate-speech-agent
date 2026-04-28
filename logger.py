import datetime

def log_result(text, output):
    with open("logs.txt", "a") as file:
        timestamp = datetime.datetime.now()
        file.write(f"{timestamp} | Input: {text} | Output: {output}\n")
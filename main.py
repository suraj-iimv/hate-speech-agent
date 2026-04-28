from model import classify_text
from logger import log_result

while True:
    user_input = input("Enter text (type 'exit' to quit): ")
    
    if user_input.lower() == "exit":
        print("Exiting...")
        break
    
    result = classify_text(user_input)
    print(result)
    
    log_result(user_input, result)
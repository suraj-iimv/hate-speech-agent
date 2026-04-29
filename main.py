from model import classify_text

while True:
    user_input = input("Enter text (type 'exit' to quit): ")
    
    if user_input.lower() == "exit":
        print("Exiting...")
        break
    
    result = classify_text(user_input)
    print(result)

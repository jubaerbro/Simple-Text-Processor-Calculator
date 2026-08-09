# main.py
import math_tools
import text_tools

def main():
    print("Welcome to Our Python Group Lab!")
    print("-" * 35)
    
    # Testing Person B's math module
    num1, num2 = 15, 5
    sum_result = math_tools.add(num1, num2)
    print(f"Math Test: {num1} + {num2} = {sum_result}")
    
    # Testing Person C's text module
    message = "github collaboration is awesome"
    shout_message = text_tools.shout(message)
    print(f"Text Test: {shout_message}")
    word_count = text_tools.count_words(message)
    print(f"Word Count Test: '{message}' has {word_count} words")
    
    print("-" * 35)
    print("Success! All modules are communicating perfectly.")

if __name__ == "__main__":
    main()

def clean_string(s):
    return ''.join(c.lower() for c in s if c.isalnum())

def is_palindrome(s):
    cleaned_s = clean_string(s)
    def check_recursive(cleaned_s, start, end):
        if start >= end:
            return True
        if cleaned_s[start] != cleaned_s[end]:
            return False
        return check_recursive(cleaned_s, start + 1, end - 1)
    
    return check_recursive(cleaned_s, 0, len(cleaned_s) - 1)

def main():
    test_phrases = [
        "saudavel leva duas",
        "A man, a plan, a canal, Panama",
        "racecar",
        "hello",
        "Was it a car or a cat I saw",
        "No 'x' in Nixon"
    ]
    for phrase in test_phrases:
        result = is_palindrome(phrase)
        print(f"'{phrase}' é um palíndromo? {result}")

if __name__ == "__main__":
    main()
s = "A man, a plan, a canal: Panama"

clean_s = [char.lower() for char in s if char.isalnum()]

print(clean_s)
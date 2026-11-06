# Ask the user for a link
url = input("Enter the link to check: ")

# We start by assuming the link is safe
is_safe = True

print("\n--- Scanning Link ---")

# 1. Check for unsecure HTTP
if "http://" in url:
    print("- WARNING: Not secure (uses http instead of https).")
    # This must be indented so it only runs IF the statement above is true
    is_safe = False

# 2. Check for hidden '@' symbol
if "@" in url:
    print("- WARNING: Uses an '@' symbol to trick you.")
    # This must also be indented
    is_safe = False

# 4. Give the final answer
print("\n--- Final Result ---")

if is_safe == True:
    print("VERDICT: The link looks SAFE.")
else:
    print("VERDICT: DANGER! This is likely a phishing link.")
import os
import sys

def main():
    # Retrieve the secret from the environment variable
    secret = os.environ.get("MY_SECRET_TOKEN")
    
    print("=========================================")
    print("      GITHUB SECRETS DEMO SCRIPT        ")
    print("=========================================\n")
    
    if not secret:
        print("❌ Error: MY_SECRET_TOKEN is not set or is empty.")
        print("Please check your GitHub Repository Secrets settings and ensure")
        print("you have added a secret named 'MY_SECRET_TOKEN'.")
        sys.exit(1)
        
    print("✅ Success: Successfully retrieved the secret token from the environment!")
    print(f"📏 Secret length: {len(secret)} characters.")
    
    # Showcase that GitHub masks the secret when printed directly
    print("\nBelow, we attempt to print the secret directly.")
    print("GitHub Actions will automatically mask this value with '***' to protect it:")
    print(f"Direct print: {secret}")
    print("\n=========================================")

if __name__ == "__main__":
    main()

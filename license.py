import hashlib
import base64
import datetime

# Secret key used for generating and verifying licenses
SECRET_KEY = "your_secret_key_here"

# Generate a license key for a user
def generate_license(username, expiration_date):
    data_to_hash = f"{username}{expiration_date}{SECRET_KEY}"
    license_key = hashlib.sha256(data_to_hash.encode()).hexdigest()
    return license_key

# Verify a license key
def verify_license(username, license_key):
    expiration_date = datetime.datetime.now()  # Current date as an example
    expected_license = generate_license(username, expiration_date)
    return license_key == expected_license

# Example usage
username = "john_doe"
expiration_date = datetime.datetime(2023, 12, 31)  # Set the expiration date
license_key = generate_license(username, expiration_date)
print(f"Generated License Key: {license_key}")

# Verify a license key
user_input_license_key = input("Enter your license key: ")
if verify_license(username, user_input_license_key):
    print("License key is valid.")
else:
    print("License key is invalid.")

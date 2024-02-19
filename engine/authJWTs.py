import jwt
import datetime
# Example secret key (should be kept secret in production)

def generate_jwt(payload, secret_key):
    
    # Encode the JWT
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

def decode_jwt(token, secret_key):
   
    try:
        # Decode the JWT
        decoded_payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return decoded_payload
    except jwt.ExpiredSignatureError:
        print("Token has expired")
        return None
    except jwt.InvalidTokenError:
        print("Invalid token")
        return None

# Example payload and secret key
secret_key = "mysecretkey"
payload = {
    "EMP_ID": 1,
    "FIRST_NAME": "John",
    "LAST_NAME": "Doe",
    "DEPARTMENT": "IT",
    "REPORTING_MANAGER": "Manager1",
    "PROJECT_MANAGER": "ProjectManager1",
    "EMAIL": "john.doe@email.com",
    "DESIGNATION": "Developer",
    "CREATED_BY": "TEST_SCHEMA",
    "CREATED_ON": "27-12-23 7:40:53.058012000 PM",
    "UPDATED_BY": "TEST_SCHEMA",
    "UPDATED_ON": "27-12-23 7:40:53.058012000 PM"
}

# Generate and print JWT token


# Decode JWT token and print decoded payload
# decoded_payload = decode_jwt(token, secret_key)
# if decoded_payload:
#     print("Decoded payload:", decoded_payload)
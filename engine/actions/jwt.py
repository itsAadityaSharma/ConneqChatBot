import jwt
import datetime
# Example secret key (should be kept secret in production)
secret_key = "mysecretkey"
# Example payload
payload = {
    "user_id": 123,
    "username": "john_doe",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)  # Expiry time
}
# Encode the JWT
token = jwt.encode(payload, secret_key, algorithm='HS256')
print("JWT token:", token)
# Decode the JWT
try:
    decoded_payload = jwt.decode(token, secret_key, algorithms=['HS256'])
    print("Decoded payload:", decoded_payload)
except jwt.ExpiredSignatureError:
    print("Token has expired")
except jwt.InvalidTokenError:
    print("Invalid token")
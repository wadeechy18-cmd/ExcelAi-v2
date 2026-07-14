from app.security.jwt import create_access_token, verify_token

token = create_access_token({"sub": "test@example.com"})

print(token)

print(verify_token(token))
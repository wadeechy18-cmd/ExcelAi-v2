from app.security.hashing import hash_password, verify_password

password = "Hello123"

hashed = hash_password(password)

print(hashed)

print(verify_password(password, hashed))
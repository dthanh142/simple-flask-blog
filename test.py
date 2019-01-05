from werkzeug.security import generate_password_hash, check_password_hash

hash = generate_password_hash('thanh0412')
print(hash)

print(check_password_hash(hash, 'thanh0412'))
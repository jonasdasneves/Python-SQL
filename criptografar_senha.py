import bcrypt

# Senha que você deseja armazenar
password = b"sua_senha_secreta"

# Gerar um salt e hash da senha
hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

# Agora você pode armazenar `hashed_password` no banco de dados
print(hashed_password)

input_password = b"sua_senha_secreta"

# Recuperar o hash armazenado no banco de dados
stored_hash = hashed_password  # O hash que você armazenou

# Verificar se a senha fornecida corresponde ao hash armazenado
if bcrypt.checkpw(input_password, stored_hash):
    print("Senha correta!")
else:
    print("Senha incorreta.")
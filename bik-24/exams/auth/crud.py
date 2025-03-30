from schemas import users, UserRegister, UserLogin
from passlib.context import CryptContext

pwd_context = CryptContext(['bcrypt'])

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password, hash_password):
    return pwd_context.verify(password, hash_password)

def create_user(user):
    users.append(UserRegister(
            name=user.name,
            email=user.email,
            password=hash_password(user.password) 
    )
    )

    print(users)

def check_user(user: UserLogin):
    result = verify_password(user.password, users[0].password)
    return result
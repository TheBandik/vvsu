from fastapi import APIRouter

from schemas import UserRegister, users, UserLogin
from crud import create_user, check_user

router = APIRouter()

# Регистрация пользователя
@router.post('/register/', tags=['User'])
def register_user(user: UserRegister):
    create_user(user)
    return {'message': 'Пользователь добавлен'}

# Получение списка пользователей
@router.get('/users/', tags=['User'])
def get_users():
    return users

# Авторизация пользователя
@router.post('/login/', tags=['User'])
def login(user: UserLogin):
    if check_user(user):
        return {'message': 'Успешная авторизация'}
    else:
        return {'message': 'Неправильная почта или пароль'}

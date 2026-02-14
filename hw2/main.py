from schemas import User

json_user_valide = {
    "name": "John Doe",
    "age": 30,
    "email": "8A2dA@example.com",
    "is_employeed": True,
    "address": {
        "city": "New York",
        "street": "Main Street",
        "house_number": 123
    }
}

json_user_not_valide = {
    "name": "John Doe",
    "age": 15,
    "email": "8A2dA@example.com",
    "is_employeed": True,
    "address": {
        "city": "New York",
        "street": "Main Street",
        "house_number": 123
    }
}

json_user_old_not_valide = {
    "name": "John Doe",
    "age": 65,
    "email": "8A2dA@example.com",
    "is_employeed": True,
    "address": {
        "city": "New York",
        "street": "Main Street",
        "house_number": 123
    }
}

def process_user_json(user_json:dict)->User:
    try:
        user = User.model_validate_json(user_json)
        return user.model_dump_json(exclude_unset=True)
    except ValueError as e:
        print(e)
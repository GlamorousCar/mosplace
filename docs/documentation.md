_Table of Contents_



# Documentation At source{d}



## Получение списка все округов 
```http
GET /api/v1/disticts
```
*Permission: AllowAny*

### Response example 
```json
[
    {
        "id": 1,
        "title": "Центральный",
        "abbreviation": "ЦАО",
        "image": "image_url"
    }, 
]
```

## Получение мест определенного округа
```http
GET /api/v1/places
```
### Query parameters 

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `district_id` | `int` | **Required**. id округа, места которого мы хотим получить|
### Examples of API calls
```http
GET /api/v1/places/?district_id=1
```
### Response example 
```json
[
    {
        "id": 2,
        "images": [
            {
                "id": 1,
                "image": "*image_url*",
                "place": 2
            }
        ],
        "title": "",
        "short_description": "",
        "full_description": "description",
        "longitude": "0.000000",
        "latitude": "0.000000",
        "type": "unique_place",
        "district": 1
    },
```



## Создание округа
```http
POST /api/v1/district_create/
```

### Headers
|Header|Value|Description|
|------|-----|------|
| Authorization|JWT {access token}|The authorization token |

### Body parameters

| Parameter | Description |
|------|-----|
| title| Required |
| abbreviation||
| image||

## Регистрация
```http
POST /auth/users/
```
### Body parameters 
| Parameter | Type | Description |
|------|-----|------|
| username or phone ot email|str| Required |
| password|character set|Required |

Если пользователь существует то ответ будет:
```json
{
    "username": [
        "A user with that username already exists."
    ]
}
```
Если это новый пользователь, то вернется:
```json
{
    "email": "",
    "username": "name",
    "id": "id"
}
```
После регистрации, аккаунт нужно будет активировать, делается это пока вручную через админку Django. Потом будет отправляться запрос на почту, с письмом-подтверждением
После активации аккаунта, необходимо будет получить JWT токен

### Получение jwt токена
```http
POST /auth/jwt/create/
```
### Body parameters 
| Parameter | Type | Description |
|------|-----|------|
| username|str| Required |
| password|character set|Required |

### Response
```json
{
    "refresh": "refresh_token",
    "access": "access_token"
}
```
Если аккаунта не существет, то вернётся ошибка:
```json
{
    "detail": "No active account found with the given credentials"
}
```
## Получение профиля 
*permission: ForAdmin, ForProfileOwner*
```http
GET /api/v1/profile/
```
### Query parameters 
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `id` | `int` | **Required**. id профиля|

### Headers
|Header|Value|Description|
|------|-----|------|
| Authorization|JWT {access token}|The authorization token |
### Examples of API calls
```http
GET /api/v1/profile/id=1
```
### Respone
```json
[
    {
        "id": "id",
        "username": "username"
    }
]
```
Если access_token неправильный, то вернётся ошибка:
```json
{
    "detail": "Given token not valid for any token type",
    "code": "token_not_valid",
    "messages": [
        {
            "token_class": "AccessToken",
            "token_type": "access",
            "message": "Token is invalid or expired"
        }
    ]
}
```





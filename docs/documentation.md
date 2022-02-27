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
GET /api/v1/district_create/
```
]
### Headers
|Header|Value|Description|
|------|-----|------|
| Authorization|JWT {access token}|The authorization token |

### fields
```json
"title": "",
"abbreviation": "",
"image": null
```








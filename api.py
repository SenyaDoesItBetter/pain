import json
import requests


class PetFriends:

    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_api_key(self, email: str, passwd: str) -> json:

        headers = {
            'email': email,
            'password': passwd,
        }
        res = requests.get(self.base_url + '/api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key: json, filter: str = "") -> json:

        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_new_pet(self, auth_key: json, name: str, animal_type: str,
                    age: str, pet_photo: str) -> json:

        data = {
            'name': 'Spike',
            'animal_type': 'dog',
            'age': '10',
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
        }
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'pet', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def delete_pet(self, auth_key: json, pet_id: str) -> json:

        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def update_pet_info(self, auth_key: json, pet_id: str, name: str,
                        animal_type: str, age: int) -> json:

        headers = {'auth_key': auth_key['key']}
        data = {
            "id": 0,
            "category": {
                "id": 0,
                "name": "spike"
            },
            "name": "dog",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "mike"
                }
            ],
            "status": "available"
        }

        res = requests.put(self.base_url + 'pets' + pet_id, headers=headers, data=data)
        print(res.status_code)
        print(res.text)
        print(res.json())
        print(type(res.json()))
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def new_pet_simple(self, auth_key: json, name: str, animal_type: str, age: int) -> json:

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }
        res = requests.post(self.base_url + '/api/create_pet_simple/', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def new_photo_of_pet(self, auth_key: json, pet_id: str, pet_photo: str):

        data = {
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
        }
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url + f'/api/pets/set_photo/{pet_id}/', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

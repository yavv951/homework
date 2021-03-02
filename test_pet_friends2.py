from Api2 import PetFriends
from setting import *

pf = PetFriends()


def test_add_new_pet_with_unvalid_data(self,name='', animal_type='',
                                     age='', pet_photo='images/123.jpg'):
    """ Тест как отреагирует система передав питомце пустые значения"""
    _, auth_key = self.pf.get_api_key(valid_email, valid_password)

    status, result = self.pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet(self):
    _, auth_key = self.pf.get_api_key(valid_email, valid_password)
    _, my_pets = self.pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        self.pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/123.jpg")
        _, my_pets = self.pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = self.pf.delete_pet(auth_key, pet_id)
    _, my_pets = self.pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(self,name='Мурзик', animal_type='Котэ', age=5):
    _, auth_key = self.pf.get_api_key(valid_email, valid_password)
    _, my_pets = self.pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = self.pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")


def test_get_api_key_for_unvalid_user(email=valid_email, password=unvalid_password):
    """Негативный тест методом GET с неправильным паролем"""
    status, result = pf.get_api_key(email, password)
    assert status == 403


def test_get_api_key_for_unvalid_email(email=unvalid_email, password=valid_password):
    """Негативный тест методом GET с неправильным логином"""
    status, result = pf.get_api_key(email, password)
    assert status == 403


def test_create_pet_simple(self,name='Барсик', animal_type='кот', age='10', pet_photo=""):
    """Методом Post создаем питомца без фото"""
    _, auth_key = self.pf.get_api_key(valid_email, valid_password)
    status, result = self.pf.create_pet_simple(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_add_photo_of_pet(pet_photo='images/123.jpg'):
    """Методом Post  добавляем фото питомцу"""
    _, auth_key = self.pf.get_api_key(valid_email, valid_password)
    _, my_pets = self.pf.get_list_of_pets(auth_key, "my_pets")
    status, result = self.pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
    assert status == 200
    assert pet_id  in myPets.values()


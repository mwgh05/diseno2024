import user

class Organization:
    def __init__(self, id, name, users, address, contact, creationDate, updateDate):
        self.id = id
        self.name = name
        self.users = users
        self.address = address
        self.contact = contact
        self.creationDate = creationDate
        self.updateDate = updateDate

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "users": self.users,
            "address": self.address,
            "contact": self.contact,
            "creationDate": self.creationDate,
            "updateDate": self.updateDate
        }

    @staticmethod
    def from_json(json_data):
        return Organization(
            json_data.get('id'),
            json_data.get('name'),
            json_data.get('users'),
            json_data.get('address'),
            json_data.get('contact'),
            json_data.get('creationDate'),
            json_data.get('updateDate')
        )

    def update_contact(self, contact_data):
        self.contact = contact_data

    def add_users(self, user_id):
        self.users.append(user_id)

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address


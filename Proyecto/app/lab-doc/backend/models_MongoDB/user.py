class User:
    def __init__(self, id, name, organization, email, creationDate, updateDate):
        self.id = id
        self.name = name
        self.organization = organization
        self.email = email
        self.creationDate = creationDate
        self.updateDate = updateDate

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "organization": self.organization,
            "email": self.email,
            "creationDate": self.creationDate,
            "updateDate": self.updateDate
        }

    @staticmethod
    def from_json(json_data):
        return User(
            json_data.get('id'),
            json_data.get('name'),
            json_data.get('organization'),
            json_data.get('email'),
            json_data.get('creationDate'),
            json_data.get('updateDate')
        )

    def update_contact(self, contact_data):
        self.email = contact_data

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_organization(self):
        return self.organization

    def set_name(self, name_data):
        self.name = name_data

    def set_email(self, email_data):
        self.email = email_data

    def set_organization(self, organization_data):
        self.organization = organization_data


from liku_backend.birthday.domain.birthday_repository import BirthdayRepository


class BirthdayRetriever:
    def __init__(self, birthday_repository: BirthdayRepository):
        self.birthday_repository = birthday_repository

    def invoke(self, birthday_id: str):
        self.birthday_repository.retrieve(birthday_id)
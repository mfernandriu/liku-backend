import abc
from typing import List

from liku_backend.birthday.domain.birthday import Birthday


# TODO when updating, and removing check that the user is the one with the right to do it?
class BirthdayRepository(abc.ABC):
    @abc.abstractmethod
    def store(self, birthday: Birthday):
        pass

    @abc.abstractmethod
    def update(self, birthday: Birthday):
        pass

    @abc.abstractmethod
    def remove(self, birthday_id: str):
        pass

    @abc.abstractmethod
    def retrieve(self, user_id: str) -> List[Birthday]:
        pass

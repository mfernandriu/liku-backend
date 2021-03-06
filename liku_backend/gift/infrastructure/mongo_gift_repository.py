from typing import List

from liku_backend.gift.domain.gift import Gift
from liku_backend.gift.domain.gift_repository import GiftRepository
from liku_backend.gift.infrastructure import gift_to_mongo_object_converter, mongo_object_to_gift_converter
from liku_backend.shared.infrastructure.mongo_repository import MongoRepository


class MongoGiftRepository(MongoRepository, GiftRepository):
    def __init__(
            self,
            host=str,
            port=int,
            user=str,
            password=str,
            database_name=str,
    ):
        collection_name = "gifts"
        super().__init__(
            host,
            port,
            user,
            password,
            database_name,
            collection_name
        )

    def store(self, gift: Gift):
        gift_as_dict = gift_to_mongo_object_converter.invoke(gift)
        self.collection.insert_one(gift_as_dict)

    def update(self, gift: Gift):
        query = {"id_": gift.id_}
        update = {
            "$set": {
                "description": gift.description,
            }
        }
        self.collection.update_one(query, update)

    def remove(self, gift_id: str):
        query = {"id_": gift_id}
        self.collection.delete_one(query)

    def retrieve(self, user_id: str, birthday_id: str, gifted: bool) -> List[Gift]:
        query = {"user_id": user_id, "birthday_id": birthday_id, "gifted": gifted}
        cursor = self.collection.find(query, {"id": False})
        gifts_as_dict = list(cursor)
        gifts = mongo_object_to_gift_converter.convert_many(gifts_as_dict)
        return gifts

    def update_as_gifted(self, gift_id: str):
        query = {"id_": gift_id}
        update = {
            "$set": {
                "gifted": True,
            }
        }
        self.collection.update_one(query, update)

    def update_as_not_gifted(self, gift_id: str):
        query = {"id_": gift_id}
        update = {
            "$set": {
                "gifted": False,
            }
        }
        self.collection.update_one(query, update)

    def remove_dangling(self, user_id, birthday_id):
        query = {"user_id": user_id, "birthday_id": birthday_id}
        self.collection.delete_many(query)

    def empty(self):
        self.collection.delete_many({})

from unittest.mock import Mock

from liku_backend.gift.application.gifted_gift_unmarker import GiftedGiftUnmarker


def test_calls_gifts_repository():
    gift_repository = Mock()
    gift_repository.update_as_not_gifted = Mock()
    gifted_gift_marker = GiftedGiftUnmarker(gift_repository)
    gift_id = "gift_id"
    gifted_gift_marker.invoke(gift_id)
    gift_repository.update_as_not_gifted.assert_called_once_with(gift_id)

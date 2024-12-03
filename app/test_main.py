import datetime
from unittest import mock
from app.main import outdated_products


def test_should_return_only_outdated_products() -> None:
    orig_date = datetime.date

    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = orig_date(2022, 2, 6)
        mock_date.side_eff = lambda *args, **kwargs: orig_date(*args, **kwargs)

        product_list = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 160
            }
        ]

        expected_outdated = ["chicken", "duck"]
        result = outdated_products(product_list)

        assert result == expected_outdated


def test_should_return_empty_list_if_no_outdated_products() -> None:
    orig_date = datetime.date

    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = orig_date(2022, 2, 6)
        mock_date.side_eff = lambda *args, **kwargs: orig_date(*args, **kwargs)

        product_list = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 6),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 120
            }
        ]

        expected_outdated = []
        result = outdated_products(product_list)

        assert result == expected_outdated

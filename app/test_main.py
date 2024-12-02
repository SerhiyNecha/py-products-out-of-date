import datetime
from unittest import mock
from app.main import outdated_products


def test_should_return_if_all_products_are_not_outdated() -> None:
    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = datetime.date(2024, 12, 2)
        product_list = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 2),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 2),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 2),
                "price": 160
            }
        ]
        outdated = []
        result = outdated_products(product_list)

        assert result == outdated


def test_should_return_if_all_products_are_outdated() -> None:
    with mock.patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = datetime.date(2024, 12, 2)
        product_list = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2024, 12, 3),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2024, 12, 2),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2024, 12, 1),
                "price": 160
            }
        ]
        outdated = ["duck"]
        result = outdated_products(product_list)

        assert result == outdated

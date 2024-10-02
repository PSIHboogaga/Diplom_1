from praktikum.bun import Bun


class TestBun:
    def test_bun_get_name(self):
        bun = Bun('Булочка "Самая сладкая и сочная, как ты"', 777)
        assert bun.get_name() == 'Булочка "Самая сладкая и сочная, как ты"', 'Unable to get bun name'

    def test_bun_get_price(self):
        bun = Bun('Булочка "Самая сладкая и сочная, как ты"', 777)
        assert bun.get_price() == 777, 'Unable to get bun price'

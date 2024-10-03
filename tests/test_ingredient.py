import pytest
from praktikum.ingredient import Ingredient
from praktikum import ingredient_types


class TestIngredient:
    def test_ingredient_get_name(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, 'Соус "Слезы твоей бывшей"', 333)
        assert ingredient.get_name() == 'Соус "Слезы твоей бывшей"', 'Название ингредиента не получено'
    def test_ingredient_get_price(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, 'Соус "Слезы твоей бывшей"', 333)
        assert ingredient.get_price() == 333, 'Цена ингредиента не получена'

    @pytest.mark.parametrize(
        'type, name, price, expected_ingredient',
        [
            [ingredient_types.INGREDIENT_TYPE_SAUCE, '"Слезы твоей бывшей"', 333, 'SAUCE'],
            [ingredient_types.INGREDIENT_TYPE_FILLING, 'Мини-салат Экзо-Плантаго', 4400, 'FILLING']
        ]
    )
    def test_ingredient_get_type(self, type, name, price, expected_ingredient):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == expected_ingredient, 'Тип ингредиента не получен'

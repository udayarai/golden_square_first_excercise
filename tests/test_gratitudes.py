from lib.gratitudes import Gratitudes

"""
when gratitue is not added
"""
def test_without_adding_gratitude():
    gratitudes = Gratitudes()
    assert gratitudes.format() == "Be grateful for: "

"""
when a single gratitude is added it returns the gratitude
"""
def test_with_single_gratitude():
    gratitudes = Gratitudes()

    gratitudes.add("food")
    assert gratitudes.format() == "Be grateful for: food"


"""
when a multiple gratitude is added it returns the gratitude
"""
def test_with_multiple_gratitude():
    gratitudes = Gratitudes()

    gratitudes.add("food")
    gratitudes.add("water")
    gratitudes.add("shelter")
    assert gratitudes.format() == "Be grateful for: food, water, shelter"

import pytest

from string_utils import StringUtils


@pytest.mark.parametrize("input, output", [ ("skypro", "Skypro"), ("Best", "Best"), (" school", " School"), ("", "")  ])
def test_capitilize(input, output):
    stringutils = StringUtils()
    res = stringutils.capitilize(input)
    assert res == output

@pytest.mark.parametrize("input, output", [(" Skypro", "Skypro"), ("  Skyeng", "Skyeng")])
def test_trim(input, output):
    stringutils = StringUtils()
    res = stringutils.trim(input)
    assert res == output

def test_to_list():
    stringutils = StringUtils()
    res = stringutils.to_list("Milk 9.5%,Pork,Salad,Water,Some vegetables")
    assert res == ["Milk 9.5%", "Pork", "Salad", "Water", "Some vegetables"]

@pytest.mark.parametrize("input, symbol, result", [("Peter", "e", True), ("Max", "d", False), ("John Simons", " ", True), ("Dominia", "O", False)])
def test_contains(input, symbol, result):
    stringutils = StringUtils()
    res = stringutils.contains(input, symbol)
    assert res == result

def test_delete_symbol():
    stringutils = StringUtils()
    res = stringutils.delete_symbol("The Rostov-on-Don", "The ")
    assert res == "Rostov-on-Don"

@pytest.mark.parametrize("input, endSymbol, result", [("Moscow", "w", True), ("Omsk", "m", False), ("Anapa", "A", False)])
def test_end_with(input, endSymbol, result):
    stringutils = StringUtils()
    res = stringutils.end_with(input, endSymbol)
    assert res == result

@pytest.mark.parametrize("input, result", [("", True), ("   ", True), ("Not true", False)])
def test_is_empty(input, result):
    stringutils = StringUtils()
    res = stringutils.is_empty(input)
    assert res == result

@pytest.mark.parametrize("input, joiner, output", [(["Saint", "Petersburg"], "-", "Saint-Petersburg"), (["It's 10", "36 pm"], ":", "It's 10:36 pm"), (["Never", "Gonna", "Give", "You", "Up"], " ", "Never Gonna Give You Up")])
def test_list_to_string(input, joiner, output):
    stringutils = StringUtils()
    res = stringutils.list_to_string(input, joiner)
    assert res == output





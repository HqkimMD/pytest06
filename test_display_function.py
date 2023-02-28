from function import display_month
import pytest

@pytest.mark.display #pytest -m display
@pytest.mark.parametrize('input_number,expected_result', [
    (1,"January"),(2,"February"),(3,"March"),(4,"April"),
    (5,"May"),(6,"June"),(7,"July"),(8,"August"),
    (9,"September"),(10,"October"),(11,"November"),
    (12,"December"),(0,"out of range"),(13,"out of range"),
    (-10,"out of range"),(22,"out of range"),
    (1.1,"input integer"),(13.1,"out of range"),
    ("a","input integer"),("#","input integer"),
    (0.5,"out of range"),(-1.5,"out of range"),
    (1.5,"input integer"),
])
def test_display(input_number, expected_result):
    actual_result = display_month(input_number)
    assert expected_result == actual_result
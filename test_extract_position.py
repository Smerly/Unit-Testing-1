import unittest
import pytest
import math
from extract_position import extract_position


def test_extract_position():
    result1 = extract_position(
        '|error| numerical calculations could not converge.')
    print(result1)
    result2 = extract_position(
        '|update| the positron location in the particle accelerator is x:21.432')
    print(f'type:{type(result2)} content:{result2}')
    assert result1 == None
    assert math.isclose(float(result2), 21.432)

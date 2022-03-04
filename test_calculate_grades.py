import unittest
from unittest import mock
import pytest
import math
from calculate_grade import *


def test_display_grade_stat():
    read_inputs = [12, 13, 41, 2, 3]
    mean, standard_deviation = display_grade_stat(read_inputs)
    assert math.isclose(mean, 14.2)
    assert math.isclose(round(standard_deviation, 3), 14.134)

from enum import Enum

from UnitTests.UnitTestModels.UnitTestModel import UnitTest


class ShowTestOf(Enum):
    ALL = [True, False]
    PASSED = [True]
    FAILED = [False]


def flatten_position(position: str):
    return position.replace(' ', '').replace('\n', '')


def assert_case(tested_case: str, calculated_case: str, case_no: int) -> UnitTest:
    try:
        assert tested_case == calculated_case
        return UnitTest(case_id=case_no, passed=True, desired_output=tested_case, output=calculated_case)
    except AssertionError:
        return UnitTest(case_id=case_no, passed=False, desired_output=tested_case, output=calculated_case)

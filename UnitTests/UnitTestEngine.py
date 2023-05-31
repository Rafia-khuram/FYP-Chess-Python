from UnitTests.UnitTestDependencies import TestsOf
from UnitTests.UnitTestModels.UnitTestSectionModel import UTestSectionModel
from UnitTests.PreCalculationAlgorithmsTests import PreCalculationTests


class UnitTestEngine:
    def __init__(self, print_test_cases: TestsOf = TestsOf.NONE,
                 print_test_case_details: TestsOf = TestsOf.NONE,
                 show_only_tests: TestsOf = TestsOf.ALL):
        self.test_results: list[UTestSectionModel] = []
        self.print_test_cases = print_test_cases
        self.print_test_case_details = print_test_case_details
        self.show_only_tests = show_only_tests

    def run_tests(self):
        self.test_results += PreCalculationTests.run_tests()

    def print_tests(self):
        for test in self.test_results:
            test.print_data(self.print_test_cases, self.print_test_case_details, self.show_only_tests)

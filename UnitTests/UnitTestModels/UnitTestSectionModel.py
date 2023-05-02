from DebugUtilities.BeautifyDependency.StringBeautify import print_by_padding
from UnitTests.UnitTestDependencies import ShowTestOf
from UnitTests.UnitTestModels.UnitTestDataModel import UTestDataModel


class UTestSectionModel:
    def __init__(self, test_title: str, u_test_data: list[UTestDataModel]):
        self.test_title = test_title
        self.u_test_data = u_test_data
        self.padding_length = 100
        self.sub_part_id = 0

    def print_data(self, print_test_cases: bool, print_test_case_detail: bool, show_only_tests: ShowTestOf):
        validated_data = self._get_validated_data(show_only_tests)
        if len(validated_data) > 0:
            print_by_padding(string=self.test_title, length=self.padding_length, sub_part=self.sub_part_id,
                             padding_char_hor='~')
            print_by_padding(string='', length=self.padding_length, start_end_only=True, sub_part=self.sub_part_id)
            for list_of_cases in validated_data:
                list_of_cases.print_data(print_test_cases=print_test_cases,
                                         print_test_case_detail=print_test_case_detail)
            print_by_padding(string='', length=self.padding_length, start_end_only=True, sub_part=self.sub_part_id)
            print_by_padding(string='', length=self.padding_length, start_end_only=False, sub_part=self.sub_part_id,
                             padding_char_hor='~')
            print()

    def _get_validated_data(self, show_only_tests: ShowTestOf) -> list[UTestDataModel]:
        validated_data_models: list[UTestDataModel] = []
        for data_model in self.u_test_data:
            validated_test_cases = data_model.get_validated_tests(show_only_tests)
            if len(validated_test_cases) > 0:
                validated_data_models.append(
                    UTestDataModel(test_case_title=data_model.test_case_title, test_cases=validated_test_cases))
        return validated_data_models

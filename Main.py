from UnitTests.UnitTestDependencies import ShowTestOf
from UnitTests.UnitTestEngine import UnitTestEngine

u_engine = UnitTestEngine(show_only_tests=ShowTestOf.ALL, print_test_cases=False, print_test_case_details=False)
u_engine.run_tests()
u_engine.print_tests()

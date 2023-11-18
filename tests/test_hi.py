from tests.base import FunctionalTest


class HiTest(FunctionalTest):
    def test_1_equal_1(self) -> None:
        self.assertEqual(1, 1)

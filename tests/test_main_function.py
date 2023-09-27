import os

import pytest
from matrix_spiral_retrieval.get_spiral_matrix import get_spiral_list


MATRIX_4X4_URL = "https://raw.githubusercontent.com/Andriy-Sydorenko/async_matrix_test_task/develop/tests/testing_examples/matrix_4x4.txt"
MATRIX_10X10_URL = "https://raw.githubusercontent.com/Andriy-Sydorenko/async_matrix_test_task/develop/tests/testing_examples/matrix_10x10.txt"


class TestGetSpiralListFunction:
    @pytest.mark.parametrize(
        "url,filepath,expected_result",
        [
            (
                MATRIX_4X4_URL,
                None,
                [10, 50, 90, 130, 140, 150, 160, 120, 80, 40, 30, 20, 60, 100, 110, 70]
            ),
            (
                MATRIX_10X10_URL,
                None,
                [10, 50, 90, 130, 10, 50, 90, 130, 10, 50, 60, 70, 80, 50, 60, 70, 80, 50, 60, 20, 140, 100, 60, 20,
                 140, 100, 60, 20, 10, 40, 30, 20, 10, 40, 30, 20, 60, 100, 140, 20, 60, 100, 140, 20, 30, 40, 10, 20,
                 30, 40, 10, 130, 90, 50, 10, 130, 90, 50, 80, 70, 60, 50, 80, 70, 110, 150, 30, 70, 110, 150, 160, 130,
                 140, 150, 160, 120, 80, 40, 160, 120, 110, 100, 90, 120, 160, 40, 80, 120, 90, 100, 110, 70, 30, 150,
                 140, 130, 10, 50, 60, 20]
            ),
            (
                None,
                os.path.join(os.getcwd(), "tests", "testing_examples", "matrix_4x4.txt"),
                [10, 50, 90, 130, 140, 150, 160, 120, 80, 40, 30, 20, 60, 100, 110, 70]
            ),
            (
                None,
                os.path.join(os.getcwd(), "tests", "testing_examples", "matrix_10x10.txt"),
                [10, 50, 90, 130, 10, 50, 90, 130, 10, 50, 60, 70, 80, 50, 60, 70, 80, 50, 60, 20, 140, 100, 60, 20,
                 140, 100, 60, 20, 10, 40, 30, 20, 10, 40, 30, 20, 60, 100, 140, 20, 60, 100, 140, 20, 30, 40, 10, 20,
                 30, 40, 10, 130, 90, 50, 10, 130, 90, 50, 80, 70, 60, 50, 80, 70, 110, 150, 30, 70, 110, 150, 160, 130,
                 140, 150, 160, 120, 80, 40, 160, 120, 110, 100, 90, 120, 160, 40, 80, 120, 90, 100, 110, 70, 30, 150,
                 140, 130, 10, 50, 60, 20]
            )
        ]
    )
    @pytest.mark.asyncio
    async def test_main_function(self, url, filepath, expected_result):
        assert await get_spiral_list(url=url, filepath=filepath) == expected_result

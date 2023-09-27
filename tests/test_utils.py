import os
import tempfile

import aiohttp
import pytest
from aioresponses import aioresponses

from matrix_spiral_retrieval._utils import _get_matrix_from_file, _get_matrix_from_url  # noqa

CORRECT_URL = "https://raw.githubusercontent.com/Andriy-Sydorenko/async_matrix_test_task/develop/tests/testing_examples/matrix_4x4.txt" # noqa


class TestGetMatrixFromUrlFunction:
    @pytest.mark.asyncio
    async def test_get_matrix_from_url_with_correct_parameters(self):
        """
        Test if function works without errors
        """

        url = CORRECT_URL
        expected_matrix_data = "1,2,3\n4,5,6\n7,8,9"

        with aioresponses() as m:
            m.get(url, body=expected_matrix_data)

            matrix_data = await _get_matrix_from_url(url)

            assert matrix_data == expected_matrix_data

    @pytest.mark.asyncio
    async def test_get_matrix_from_url_invalid_extension(self):
        """
        Test if function throws an exception when URL extension is incorrect
        """

        url = "https://example.com/matrix.csv"

        with pytest.raises(aiohttp.InvalidURL):
            await _get_matrix_from_url(url)

    @pytest.mark.asyncio
    async def test_get_matrix_from_url_invalid_url(self):
        """
        Test if URL is invalid
        """

        url = "https://some_url.com/matrix.txt"

        with aioresponses() as m:
            m.get(url, status=404)

            with pytest.raises(aiohttp.ClientError):
                await _get_matrix_from_url(url)

    @pytest.mark.asyncio
    async def test_get_matrix_from_url_throws_client_connection_error(self):
        """
        Test if function throws an exception when URL ClientConnectionError occurs
        """

        url = "https://example.com/matrix.txt"

        with aioresponses() as m:

            m.get(url, exception=aiohttp.ClientConnectionError)

            with pytest.raises(aiohttp.ClientError):
                await _get_matrix_from_url(url)

    @pytest.mark.asyncio
    async def test_get_matrix_from_url_throws_server_connection_error(self):
        """
        Test if function throws an exception when URL ServerConnectionError occurs
        """
        url = "https://example.com/matrix.txt"
        with aioresponses() as m:

            m.get(url, exception=aiohttp.ServerConnectionError)

            with pytest.raises(aiohttp.ClientError):
                await _get_matrix_from_url(url)


class TestGetMatrixFromFileFunction:

    @pytest.mark.asyncio
    async def test_get_matrix_from_file_success(self):
        """
        Test case for an existing file
        """
        content = "Test text"

        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
            temp_file.write(content.encode())
            temp_file.flush()

            text = await _get_matrix_from_file(temp_file.name)

        assert text == content

    @pytest.mark.asyncio
    async def test_get_matrix_from_file_non_existing_file(self):
        """
        Test case for a non-existing file (FileNotFoundError)
        """

        with pytest.raises(FileNotFoundError):
            await _get_matrix_from_file("not_existing_file.txt")

    @pytest.mark.asyncio
    async def test_get_matrix_from_file_empty_file(self):
        """
        Test case for handling empty file
        """

        content = ""
        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
            temp_file.write(b"")
            temp_file.flush()

            text = await _get_matrix_from_file(temp_file.name)
        assert text == content

    @pytest.mark.asyncio
    async def test_get_matrix_from_file_large_file(self):
        """
        Test case for handling large file
        """

        large_file_path = "large_file.txt"
        with open(large_file_path, "wb") as file:
            file.write(b"X" * 10_000_000)

        content = await _get_matrix_from_file(large_file_path)
        assert len(content) == 10_000_000
        os.remove(large_file_path)

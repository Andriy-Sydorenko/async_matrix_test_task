import asyncio
import os
import re
import traceback

import aiofiles
import aiohttp


async def _get_matrix_from_url(url: str) -> str:
    try:
        if not url.endswith(".txt"):
            raise ValueError("Given file must have .txt extension!")

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                matrix_data = await response.text()
                return matrix_data

    except (aiohttp.InvalidURL, ValueError) as error:
        raise aiohttp.InvalidURL(
            "Given invalid URL! Maybe it's not link to a txt file!"
        ) from error
    except (aiohttp.ClientConnectionError,
            aiohttp.InvalidURL,
            aiohttp.ClientResponseError,
            aiohttp.ServerConnectionError,
            aiohttp.ClientConnectorError) as error:
        raise aiohttp.ClientError(
            f"{type(error).__name__}: {error}"
        ) from error


async def _get_matrix_from_file(filepath: str) -> str:
    try:
        if not filepath.endswith(".txt"):
            raise ValueError("Given file must have .txt extension!")

        async with aiofiles.open(filepath, "r") as file:
            content = await file.read()
            return content

    except (IsADirectoryError,
            FileNotFoundError,
            ValueError,
            PermissionError) as error:
        traceback_str = traceback.format_exc()
        raise type(error)(f"{error}\n{traceback_str}") from error


async def _transform_matrix_to_normal(
        url: str = None,
        filepath: str = None
) -> list[list[int]]:
    matrix_data = ""
    if url:
        matrix_data = await _get_matrix_from_url(url)
    elif filepath:
        matrix_data = await _get_matrix_from_file(filepath)

    formatted_matrix = []
    split_text = matrix_data.strip().split("\n")
    for i in range(len(split_text)):
        if i % 2 == 1:
            formatted_matrix.append(
                [int(i) for i in re.findall(r"\d+", split_text[i])]
            )

    return formatted_matrix

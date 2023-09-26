import re

import aiofiles
import aiohttp


async def _get_matrix_from_url(url: str) -> str:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                matrix_data = await response.text()
                return matrix_data

    except (aiohttp.ClientConnectionError, aiohttp.ClientResponseError, aiohttp.ServerConnectionError, aiohttp.ClientConnectorError) as error:
        raise error(f"{type(error).__name__}: {error}")


async def _get_matrix_from_file(filepath: str) -> str:
    if not filepath.endswith(".txt"):
        raise ValueError("Given file must have .txt extension!")

    async with aiofiles.open(filepath, "r") as file:
        content = await file.read()
        return content


async def _transform_matrix_to_normal(url: str = None, filepath: str = None) -> list[list[int]]:
    matrix_data = ""
    if url:
        matrix_data = await _get_matrix_from_url(url)
    elif filepath:
        matrix_data = await _get_matrix_from_file(filepath)

    formatted_matrix = []
    split_text = matrix_data.strip().split("\n")
    for i in range(len(split_text)):
        if i % 2 == 1:
            formatted_matrix.append([int(i) for i in re.findall(r"\d+", split_text[i])])

    return formatted_matrix

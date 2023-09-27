# Retrieving spiral matrix

*Python package that allows to extract matrix from local file or url, and iterate spirally through it.*

## Usage

1. Clone git repo using this command:
```shell
git clone https://github.com/Andriy-Sydorenko/async_matrix_test_task
```

2. Open project in your IDE and create venv.
```shell
python -m venv venv
```

3. Activate venv:
- on Windows
    ```shell
    venv\Scripts\activate
    ```
- on macOS
    ```shell
    source venv/bin/activate
    ```

4. Install requirements:
```shell
pip install -r requirements.txt
```

## Notes
> NOTE: for security purposes, preferably, use only public URLs, avoid using ones with private information, such as tokens, user id, etc.

> NOTE: when using function, specify whether it's url or filepath, e.g.:
> 
> `get_spiral_list(url=<some_url>)`
> 
> or
> 
> `get_spiral_list(filepath=<some_path>)`
> 
> If both are specified, function will use url.

## Possible improvements:
- Logging and traceback libraries can be added for better exception handling
- More security related features can be added, to avoid displaying confidential information in the traceback

## src layout

Write library code as packages that will be subdirectories under `src` folder in root.

`.env` file helps with setting `PYTHONPATH` correctly so all packages are visible in VS code test discovery.

Setup virtual environment with `python3 -m venv .venv`.
Setup pytest and autopep8(for autoformatting) using `pip install -r requirements.txt`

Execute tests using:
```bash
python -m unittest tests
# or
PYTHON=src pytest
```
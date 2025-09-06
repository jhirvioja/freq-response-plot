# freq-response-plot

A command-line tool that takes a .csv with header `frequency,raw` and generates a frequency chart in png.

## Quickstart

1. Install [uv](https://docs.astral.sh/uv/) (if not installed)
2. Clone repo, install dependencies with `uv sync` (a venv will be created by default)
3. Run the script with `uv run main.py input_data.scv` (uses venv by default)
4. A cleaned plot will be outputted as csv alongside with a png frequency chart

# Kidney Disease Classification

Authors: Carmen Zhang, Graham Greene, June Lynn, Richard von Celsing

# About:

***(\*\* A short paragraph (view from 10,000 feet) that says what question you asked, what you found at a high level, and 1-2 sentences on what the findings might mean.)***

# Report

The final report can be found here (HTML and PDF) ***\*\* to do add link to HTML and PDF. \*\****

# Usage

### Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) (version 0.12 or higher), which manages Python and all packages
- [Quarto](https://quarto.org/docs/get-started/) (version 1.10 or higher), which renders the report

### Run the analysis

1. Clone this repository and move into it:

    ``` bash
    git clone https://github.com/UBC-MDS-2026-27/DSCI-522-kidney_disease_classification.git
    cd DSCI-522-kidney_disease_classification
    ```

2. Create the virtual environment (run from the root of the repository):

    ``` bash
    uv sync
    ```

3. Run the analysis and render the report:

    ``` bash
    uv run quarto render analysis/kidney-disease-classification.qmd
    ```

Rendering runs the whole analysis from scratch. It downloads the data from the UCI Machine Learning Repository to `data/raw/`, writes the processed training and test sets to `data/processed/`, and creates the report at `analysis/kidney-disease-classification.html`. Existing files in those locations are overwritten.

### Optional

The raw data are already included in `data/raw/`. To re-download them without rendering the report:

``` bash
uv run python scripts/download_data.py
```

The `notebooks/` folder contains our exploratory work (EDA and modelling). It is not part of the report. To open it:

``` bash
uv run jupyter lab
```

# Dependencies

- uv (version 0.12 or higher)

- Quarto (version 1.10 or higher)

- Python 3.14 and packages listed in `pyproject.toml` (exact versions are locked in `uv.lock` and installed by `uv sync`)

# License

This project uses two licenses:

- **Software code:** The code in this repository is licensed under the MIT License.

- **Report and written content:** The project report and other non-code written content are licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) License.

See [LICENSE.md](LICENSE.md) for the full license terms.

**Exceptions:**

- **Data:** The Chronic Kidney Disease data set in `data/` is not covered by the licenses above. It was created by Rubini, Soundarapandian, and Eswaran (2015), is available from the [UCI Machine Learning Repository](https://doi.org/10.24432/C5G020), and is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- **Code of Conduct:** [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) is adapted from the Python Software Foundation Code of Conduct and, as required by its license, is shared under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).

# AI use statement:

We used Anthropic [Claude Code](https://claude.com/claude-code) Opus 5.5 to help adapt this project from conda and Jupyter to uv and Quarto. All AI-generated changes were reviewed, tested, and edited by the authors, who take full responsibility for the content of this repository.

Our instructions for the AI assistant are in [`CLAUDE.md`](https://github.com/UBC-MDS/DSCI_522_project-template-breast-cancer-predictor/blob/0.0.1/CLAUDE.md). Asking the assistant to act as a tutor rather than do the work: to guide us step by step, explain why, and critique our work honestly.

# References

***\*\* Please add \*\****

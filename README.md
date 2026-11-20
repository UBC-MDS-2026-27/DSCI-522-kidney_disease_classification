# Kidney Disease Classification

Authors: Carmen Zhang, Graham Greene, June Lynn, Richard Von Celsing

# About:

***(\*\* A short paragraph (view from 10,000 feet) that says what question you asked, what you found at a high level, and 1-2 sentences on what the findings might mean.)***

# Report

The final report can be found here (HTML and PDF) ***\*\* to do add link to HTML and PDF. \*\****

# Usage

First time running the project, install uv and Quarto, then clone this repository and move into it:

``` bash
git clone https://github.com/UBC-MDS-2026-27/DSCI-522-kidney_disease_classification.git
cd DSCI-522-kidney_disease_classification
```

Then run the following from the root of this repository to create the virtual environment:

``` bash
uv sync
```

To run the analysis and render the report, run the following from the root of this repository:

``` bash
uv run quarto render 
```

***\*\* Require attention and updates \*\**** Rendering runs the whole analysis from scratch: it downloads the data again from the (UCI Machine Learning) Repository, and overwrites the files in data/raw/ and data/processed/. The rendered report is written to ***reports/xxx.html*** and ***reports/xxxxx.pdf***, replacing the versions in this repository.

# Dependencies

***\*\* this part need attention / update, if needed \*\****

- uv (version 0.12 or higher)

- Quarto (version 1.10 or higher)

- Python and packages listed in pyproject.toml (exact versions are locked in uv.lock)

# License:

This project uses two licenses:

- **Software code:** The code in this repository is licensed under the MIT License.

- **Report and written content:** The project report and other non-code written content are licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) License.

See [LICENSE.md](LICENSE.md) for the full license terms.

# AI use statement:

We used Anthropic [Claude Code](https://claude.com/claude-code) Opus 5.5 to help adapt this project from conda and Jupyter to uv and Quarto. All AI-generated changes were reviewed, tested, and edited by the authors, who take full responsibility for the content of this repository.

Our instructions for the AI assistant are in [`CLAUDE.md`](https://github.com/UBC-MDS/DSCI_522_project-template-breast-cancer-predictor/blob/0.0.1/CLAUDE.md). Asking the assistant to act as a tutor rather than do the work: to guide us step by step, explain why, and critique our work honestly.

# References

***\*\* Please add \*\****

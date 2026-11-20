# Kidney Disease Classification

Authors: Carmen Zhang, Graham Greene, June Lynn, Richard von Celsing

# About:

In this project we build a classification model using a logistic regression algorithm which uses patient tests and information to predict whether a patient has chronic kidney disease. In practice, if a patient is determined to likely have chronic kidney disease based on the model, a clinician and evaluate them and do further testing. On a held-out test set, our final classifier had a recall of 0.92 and an F2 score (beta = 2) of 0.88. Of the 63 patients in the test set with chronic kidney disease, the model predicted 58 of them correctly (true positives) and 5 incorrectly (false negatives), giving a recall of 0.92. The decision threshold of the model was tuned explicitly to minize false negative predictions because they are most harmful in this context where patients with chronic kidney disease who are classified incorrectly could result in delayed treatment and avoidable adverse health outcomes.

The dataset used in this project contains patient lab tests, information and response labels created by L. Rubini, P. Soundarapandian, and P. Eswaran who contributed it to the UCI Machine Learning Repository in 2015. The dataset was accessed from that repository for this project and can be accessed [here](https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease). Each row in the dataset corresponds to one patient and contains features related to demographics, vital signs, blood and urine tests, and medical history.

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

We used AI as a learning and supporting tool rather than to complete the work for us. We asked AI to guide us step by step, explain concepts, help debug errors, and provide feedback on our code and reasoning. For example, our prompts included "Guide me step by step rather than give me the answer" and "Help me understand the error and explain how to fix it." We also asked AI to identify mistakes and suggest improvements. All final decisions, code, and written work remain the responsibility of our team.

# References

GBD Chronic Kidney Disease Collaboration. 2020. "Global, Regional, and National Burden of Chronic Kidney Disease, 1990–2017: A Systematic Analysis for the Global Burden of Disease Study 2017." *The Lancet* 395 (10225): 709–733. https://doi.org/10.1016/S0140-6736(20)30045-3.

Kovesdy, Csaba P. 2022. "Epidemiology of Chronic Kidney Disease: An Update 2022." *Kidney International Supplements* 12 (1): 7–11. https://doi.org/10.1016/j.kisu.2021.11.003.

Qin, Jiongming, Lin Chen, Yuhua Liu, Chuanjun Liu, Changhao Feng, and Bin Chen. 2020. "A Machine Learning Methodology for Diagnosing Chronic Kidney Disease." *IEEE Access* 8: 20991–21002. https://doi.org/10.1109/ACCESS.2019.2963053.

Rubini, L., P. Soundarapandian, and P. Eswaran. 2015. "Chronic Kidney Disease." UCI Machine Learning Repository. https://doi.org/10.24432/C5G020.

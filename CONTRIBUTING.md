# Contributing

Thanks for your interest in our chronic kidney disease classification project! We welcome bug reports, improvements to the analysis, and fixes to the documentation from anyone. By taking part, you agree to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Reporting a bug

First, search the [existing issues](https://github.com/UBC-MDS-2026-27/DSCI-522-kidney_disease_classification/issues) to see whether the problem has already been reported. If not, open a new issue that includes:

- what happened, and what you expected to happen;
- the steps we can follow to reproduce the problem;
- your operating system (e.g., macOS 15 or Windows 11); and
- the command that failed, with its full error message pasted as text.

## Suggesting a change

Before starting work on a new idea, open an issue that describes the change and explains why it would help the project. This lets the team discuss it first, so that no effort is wasted on a change that does not fit or that someone else is already making.

## Submitting your work

1. Team members create a branch in this repository; outside contributors fork the repository first. Use a name that describes the work, such as `fix-readme-usage`.
2. Keep each branch to one small, focused change, and write commit messages that say what changed (e.g., `Add boxplot of hemoglobin by class`).
3. Edit the Quarto source file (`analysis/kidney-disease-classification.qmd`), not the rendered HTML or PDF, and not `docs/index.html`.
4. Before opening a pull request, render the report in the container (see [Rendering the report](#rendering-the-report)) to check that the whole analysis still runs.
5. Open a pull request into `main` that explains your change and links its issue with `Closes #N`.
6. At least one team member must review and approve the pull request before it is merged. Nobody pushes directly to `main`.

## Setting up the project

We develop inside the same Docker container that we use to run the analysis, so everyone works with the same versions of Python, Quarto and every package. You do not need to install any of them on your own computer.

To get started, follow the [Usage section of the README](README.md#usage). It explains how to install Docker, clone the repository, create an ssh key and download our image with `docker compose pull`. Run every command in this guide from the root of the repository unless it says otherwise.

## Working in the container with Positron

We write and run code in [Positron](https://positron.posit.co/download.html), connected to the running container over ssh. The repository folder on your computer appears inside the container as `/workspace`, so any change you make there is saved to your own copy of the repository.

### One-time setup

1. Install Positron. Its Remote SSH feature is built in, so no extension is needed.
2. Make sure you have completed the README's Usage steps: an ssh key exists at `~/.ssh/id_ed25519.pub`, and you have run `docker compose pull`.
3. Make sure Git knows who you are. In a terminal on your computer, run `git config --global user.email`, which should print the email address linked to your GitHub account. If it prints nothing, set your name and email:

   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```

   Our `docker-compose.yml` shares your `~/.gitconfig` with the container, so commits you make inside it are credited to you.

### Connecting each time you work

1. Open Docker Desktop, then start the container in the background:

   ```bash
   docker compose up -d
   ```

   You can confirm it is running with `docker compose ps`, which should list `analysis-env`.
2. In Positron, click the `><` icon in the bottom-left corner of the window and choose **Connect to Host**.
3. Enter `root@localhost:2222`. A new Positron window opens, and you continue in that new window. If you are asked for the remote platform, choose **Linux**; if you are asked to trust the host's fingerprint, click **Continue**. On your first connection, Positron installs its server in the container, which can take several minutes.
4. Open the project. The window is connected (the bottom-left corner shows `SSH: localhost:2222`), but no folder is open yet and the terminal starts in `/root`. Click **Open Folder** in the Explorer, replace the path with `/workspace`, and confirm (you may need to click **OK** more than once). After the window reloads, the Explorer shows the project files.
5. Trust the folder. The first time you open `/workspace`, Positron starts in Restricted Mode, and the Welcome page says that the Python extension is not available. Click **Manage** in the grey banner at the top of the window (or **Restricted Mode** in the bottom-left corner) and choose **Trust**.
6. Choose the Python interpreter, and check it every time you connect. The most reliable way is to open the Command Palette (`Cmd+Shift+P` on macOS, `Ctrl+Shift+P` on Windows), run **Python: Select Interpreter**, choose **Enter interpreter path...**, and type `/opt/venv/bin/python`. Positron then starts a Python console with this interpreter automatically. You can also click the interpreter button in the top-right corner (it says **Start Session** before any session is running) and choose **New Console Session...**, but check the path: the environment from your own computer (`/workspace/.venv`) has the same name, `Python 3.14 (uv: dsci-522-kidney-disease-classification)`, and does not work in the container. Also avoid `/usr/bin/python3`, the container's system Python. Running `import sys; print(sys.executable)` in the Console should print `/opt/venv/bin/python`.
7. Work as usual. The Terminal, the Console and the **Render** button all run inside the container.
8. When you finish, close the Positron window, then stop and remove the container from a terminal on your computer with `docker compose down`. Your files are safe, because they live in your repository folder.

### Troubleshooting the connection

- **`~/.ssh/id_ed25519.pub` or `~/.gitconfig` turned into a folder.** Docker creates an empty folder when the file does not exist yet. Run `docker compose down`, delete the folder, create the missing file (the ssh key as described in the README, or your Git name and email as described above), and start again.
- **Positron asks for a password.** The container cannot find your public key. Check that it is named `id_ed25519.pub`, or point `docker-compose.yml` to your key's actual path.
- **"Remote host identification has changed".** This appears after you download a new image. Run `ssh-keygen -R "[localhost]:2222"` and connect again.
- **GitHub asks you to sign in when you push from the container.** Sign in once in the browser window that Positron opens; it remembers you afterwards.
- **The Console says "failed to start" and mentions `/workspace/.venv/bin/activate` and `python: command not found`.** Positron picked the `.venv` environment from your own computer. It has the same name as the container's environment, `Python 3.14 (uv: dsci-522-kidney-disease-classification)`, so check the path: run **Python: Select Interpreter**, choose **Enter interpreter path...**, type `/opt/venv/bin/python`, and start a new console session. To avoid this, you can delete the local `.venv` folder from a terminal on your computer (`rm -rf .venv`); it is ignored by Git, and `uv sync` recreates it if you need it.
- **Open Folder shows your computer's file browser (Finder or File Explorer).** You are still in the local window, not the one connected to the container. Switch to the window whose bottom-left corner shows `SSH: localhost:2222`, or connect again as described above.
- **Port 2222 is already in use.** Change the first `2222` in `docker-compose.yml` to another number (e.g., `2223`) and connect to that port. Do not commit this change.
- **Using a Linux laptop.** ssh refuses the key because the mounted file belongs to your user rather than `root`. Check that the `StrictModes no` line in the `Dockerfile` does not start with `#`. If it does, remove the `#` and push, so the workflow publishes a fixed image.

For more background, see [Working in a container over ssh with Positron](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/containers-ssh-positron.html).

## Rendering the report

To re-run the full analysis and render the report without opening Positron, run:

```bash
docker compose run --rm analysis-env uv run quarto render analysis/kidney-disease-classification.qmd
```

The `--rm` flag removes the container automatically once rendering finishes. Inside Positron, you can run the same `uv run quarto render ...` command in the Terminal from `/workspace`.

## Adding or updating a package

The image contains exactly the packages recorded in our lock files, so changing the environment always goes through a branch and a pull request:

1. On a new branch, add the package from inside the container by running `uv add <package>==<version>` in the Terminal. This pins the exact version in `pyproject.toml` and updates `uv.lock`. Commit `pyproject.toml` and `uv.lock` together.
2. Push the branch. GitHub Actions builds a new image for both Intel/AMD and ARM computers, publishes it on Docker Hub, and commits the new `sha-` image tag to `docker-compose.yml` on your branch.
3. After the workflow finishes, run `git pull` to get that commit and `docker compose pull` to download the new image. Always pull before committing again on the branch, because the workflow has added a commit of its own.
4. Open a pull request. Once it is merged, the workflow runs again on `main` and commits another new tag. When that run finishes, everyone runs `git pull` on `main` and `docker compose pull`.

## Publishing the report

Our [report on GitHub Pages](https://ubc-mds-2026-27.github.io/DSCI-522-kidney_disease_classification/) is served from `docs/index.html`, which is a copy of the rendered report and does not update by itself. Each time you re-render the report, copy the new version into `docs/` and include it in your pull request:

```bash
cp analysis/kidney-disease-classification.html docs/index.html
```

## AI policy

You may use generative AI tools (e.g., ChatGPT, Claude, or Copilot) to help write or debug code, draft text, or explain errors. If you do:

- **Disclose it.** Say in your pull request description which tool you used and what for. Significant AI use is also recorded in the AI use statement in our [README](README.md).
- **Take responsibility for it.** You are fully responsible for everything you submit. Read, test, and understand any AI-generated code or text before submitting it, and make sure you can explain it to a reviewer. Check that every reference is real and supports the claim it is cited for; AI-invented citations are not accepted.
- **Keep humans in charge.** Issues and pull requests are opened, reviewed, and merged by people, never by an AI agent or chat bot. AI tools may help check code before merging, but they never approve or merge a pull request.

## Attribution

This guide was written by our team for the DSCI 522 course at the University of British Columbia. The sections on working in the container, adding packages and publishing the report are adapted from the `CONTRIBUTING.md` of the course's [DSCI_522_project-template-breast-cancer-predictor](https://github.com/UBC-MDS/DSCI_522_project-template-breast-cancer-predictor/tree/main) example project.
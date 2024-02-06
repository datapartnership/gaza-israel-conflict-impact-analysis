# CONTRIBUTING

Thank you for considering contributing to this project! Your involvement helps improve the overall quality and functionality of the project and its codebase. Please take a moment to review the following guidelines to ensure a collaborative contribution process.

## Code of Conduct

Please note that we have a [Code of Conduct](CODE_OF_CONDUCT.md) in place. We expect all contributors to adhere to it, both in interactions within this project and in interactions with other project members to promote a welcoming and inclusive environment for everyone.

## How Can I Contribute?

There are several ways you can contribute to this project:

- **🐞 Bug Reports:** If you encounter a bug or unexpected behavior, please open an issue on GitHub. Be sure to include as much detail as possible to help us identify and fix the problem.

- **✨ Feature Requests**: If you have an idea for a new feature or enhancement, please open an issue on GitHub. Describe the feature and its use case in detail.

- **🏗️ Pull Requests (PR):** If you'd like to contribute code or documentation changes, we encourage you to submit a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).

- **📖 Documentation:** If you find any errors or have suggestions for improving our documentation, you can submit changes directly through a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).

- **📣 Community Engagement:** Pose questions, help othe contributors and engage with the community on our [Discussions](https://github.com/orgs/worldbank/discussions).

## Contributing to the Code and Documentation

Whether you are novice and expert, your contribution is valuable. If you're contributing code, we recommend getting started with [GitHub Guides](https://github.com/git-guides), [GitHub Skills](https://skills.github.com/), [GitHub Desktop](https://desktop.github.com) and/or [GitHub Docs](https://docs.github.com/en/get-started). In special, see also [collaborating with pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests). When ready, you may follow these guidelines:

1. **[Fork the Repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)**: Click the "Fork" button on the top-right corner of this repository on GitHub. This will create a copy of the project in your GitHub account. Then, clone or download this repository to your local machine. Then, navigate to the root directory of the repository.

2. **[Create a Branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository):** Create a new branch for your feature or bug fix. Use a clear and descriptive name for your branch, like `feature/new-feature`.

3. **Code Review and Changes:** Make your code changes and ensure they adhere to our coding standards.

4. **Test:** Ensure that your changes do not break existing functionality.

5. **[Commit and Push](https://github.com/git-guides/git-commit):** Commit your changes with a clear and concise commit message. Reference any related issues or pull requests in your commit message. Push your branch to your forked repository on GitHub.

6. **[Create a Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request):** Open a pull request against the main branch of this repository. Provide a clear description of your changes and reference any relevant issues. Your PR will be reviewed by maintainers.

7. **[Review and Iterate](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/requesting-a-pull-request-review):** Expect feedback and be prepared to make additional changes if necessary. We may request changes, and once everything looks good, your PR will be merged.

### Running Notebooks Locally

This repository provides a Conda/Mamba environment configuration to ensure consistent dependencies across different environments. [Conda](https://docs.conda.io)/[Mamba](https://mamba.readthedocs.io) are prevalent (interoperable) package managers. If haven't installed either, you may follow the installation instructions on the respective documentation.

To run the notebooks locally, after (1) and (2) above, please follow these steps:

- Create (or update) the environment:

  ```shell
  mamba env create -f notebooks/environment.yml
  ```

  This command will create a new environment based on the specifications provided in the `environment.yml` file.
  
- [Activate the environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment), run [JupyterLab](https://jupyterlab.readthedocs.io) and execute `notebooks`:

  ```shell
    jupyterlab
  ```

### Building Documentation Locally

To build the documentation locally, after (1) and (2) above, please follow these steps:

- Install the documentation dependencies:

  ```shell
    pip install -r docs/requirements/xt
  ```

- Build the documentation:

  ```shell
    jupyter-book build . --config docs/_config.yml --toc docs/_toc.yml
  ```

The generated documentation will be available in the `_build/html` directory. Open the `index.html` file in a web browser to view it.

## Contributing Code

Whether you are novice and expert, your contribution is valuable. If you're contributing code, please follow these guidelines:

1. **Fork the Repository**: Click the "Fork" button on the top-right corner of this repository on GitHub. This will create a copy of the project in your GitHub account.

2. **Create a Branch:** Create a new branch for your feature or bug fix. Use a clear and descriptive name for your branch, like `feature/my-new-feature` or `bugfix/issue-123`.

3. **Make Changes:** Make your code changes and ensure they adhere to our coding standards.

4. **Test:** Ensure that your changes do not break existing functionality and add tests for new features or bug fixes.

5. **Commit and Push:** Commit your changes with a clear and concise commit message. Reference any related issues or pull requests in your commit message. Push your branch to your forked repository on GitHub.

6. **Create a Pull Request:** Open a pull request against the main branch of this repository. Provide a clear description of your changes and reference any relevant issues. Your PR will be reviewed by maintainers.

7. **Review and Iterate:** Expect feedback and be prepared to make additional changes if necessary. We may request changes, and once everything looks good, your PR will be merged.

## Licensing

By contributing to this project, you agree that your contributions will be licensed under the project's [LICENSE](LICENSE).

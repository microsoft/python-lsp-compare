# Contributing to python-lsp-compare

Thank you for your interest in contributing to **python-lsp-compare**!

This repository exists to support **vendor-neutral comparison** of Python Language
Server Protocol (LSP) implementations. Contributions from maintainers of any Python
language server are welcome.

## Project Principles

When contributing, please keep the following principles in mind:

- This repository **does not define a specification** or normative behavior.
- Test cases are intended to **surface behavioral differences**, not to declare a
  single implementation as correct.
- Results are data. Interpretation and conclusions are left to users.

## Ways to Contribute

You can contribute by:

- Adding new benchmark suites or scenarios
- Improving existing test coverage
- Adding adapters or configuration for additional language servers
- Submitting benchmark results
- Improving documentation

## Submitting Benchmark Results

Benchmark results should be:

- Generated using the committed tooling
- Clearly labeled with the language server name and version
- Machine-readable (JSON)
- Submitted without editorial commentary in the same pull request

Discussion about results is welcome in issues or discussions.

## Pull Request Guidelines

- Keep pull requests focused and scoped
- Avoid combining unrelated changes
- Include documentation updates where appropriate
- Be respectful of differing implementation approaches

## Code of Conduct

This project follows the
[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
By participating, you are expected to uphold this code.

## Contributor License Agreement (CLA)

Most contributions to Microsoft projects require you to agree to a
Contributor License Agreement (CLA).

You will be prompted automatically if a CLA is required when submitting a pull request.

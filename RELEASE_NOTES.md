# ClearDocs v0.1.0

First CLI release for setting up project documentation with MkDocs and Material.

- Initialize minimal or standard documentation scaffolds.
- Reuse an existing README as the documentation homepage.
- Generate a README with protection against accidental overwrites.
- Preview locally and run strict documentation builds.
- Generate GitHub Actions workflows for GitHub Pages deployment.
- Support Python 3.10 and newer.

## Release checklist

Before publishing the GitHub release:

1. Configure a PyPI pending Trusted Publisher at https://pypi.org/manage/account/publishing/:
   - Project name: `cleardocs`
   - GitHub owner: `montymi`
   - Repository: `ClearDocs`
   - Workflow filename: `release.yml`
   - Environment name: `pypi`
2. Create the `pypi` environment in the repository's GitHub Settings > Environments.
3. Create a GitHub release targeting the packaging commit on `main`, with tag
   `v0.1.0` and title `ClearDocs v0.1.0`. Use the opening section of this file as
   the release description. Publishing the release triggers the package workflow.
4. Confirm the build and publish jobs succeed, then verify in a fresh environment:

   ```bash
   python -m pip install cleardocs==0.1.0
   cleardocs --version
   cleardocs init demo --hosting github-pages
   cleardocs build -f demo/mkdocs.yml --strict
   ```

If the PyPI project name cannot be registered, choose an available distribution
name and update setup.py, release workflow URL, and installation documentation
before creating the release. No PyPI API token is required for Trusted Publishing.

# PyPI Configuration Instructions

To publish the package to PyPI, you need to set up a `.pypirc` file in your home directory.

1. Create a file named `.pypirc` in your home directory (`C:\Users\newye\.pypirc`):

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = your-pypi-token-here

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = your-testpypi-token-here
```

2. **Important**: For TestPyPI, you need to generate a separate token at https://test.pypi.org/manage/account/token/

3. The PyPI token you were using (`pypi-AgEIcHlwaS5vcmcCJDg0MjllN...`) is for the main PyPI repository, not for TestPyPI.

4. Build and upload commands:

```bash
# Build the package
python -m build

# Upload to TestPyPI (after adding the TestPyPI token)
twine upload --repository testpypi dist/*

# Upload to main PyPI
twine upload dist/*
```

5. Never include tokens in your pyproject.toml file - they should only be in the `.pypirc` file in your home directory. 
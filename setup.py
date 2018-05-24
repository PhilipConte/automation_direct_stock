import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="automation_direct_stock",
    version="0.0.1",
    author="Philip Conte",
    author_email="philipmconte@gmail.com",
    description="package checks Automation Direct's products' availability",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PhilipConte/automation_direct_stock",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
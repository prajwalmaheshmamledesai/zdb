from setuptools import setup, find_packages

setup(
    name="zdb",  # Replace with your project name
    version="0.1.0",
    author="Prajwal",
    author_email="pmamledesai@roku.com",
    description="ZDB scripts",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/prajwalmaheshmamledesai/zdb",  # Replace with your URL
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
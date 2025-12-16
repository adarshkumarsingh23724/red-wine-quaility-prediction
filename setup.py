from setuptools import setup, find_packages

def get_requirements(file_path="requirements.txt"):
    with open(file_path) as f:
        return f.read().splitlines()

setup(
    name="redwinequalityprediction",
    version="0.1.0",
    description="ML project to predict red wine quality using physicochemical properties",
    author="Adarsh Kumar Singh",
    author_email="adarshkumar23724@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements(),
    python_requires=">=3.8",
    license="MIT",   # ✅ SPDX license expression
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
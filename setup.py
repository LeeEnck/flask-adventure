import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="sheol-adventure"
    version="0.0.1",
    author="Lee Enck",
    author_email="eaglesfootball@gmail.com",
    url="https://github.com/LeeEnck/flask-adventure",
    description="web application configured to be deployed to Heroku",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)

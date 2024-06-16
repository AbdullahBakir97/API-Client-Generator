from setuptools import setup, find_packages

setup(
    name='api-client-generator',
    version='1.0.0',
    description='A tool to automatically generate client libraries for RESTful APIs based on OpenAPI/Swagger specifications',
    author='Your Name',
    author_email='your.email@example.com',
    package_dir={'':'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'pyyaml',
        'jinja2',
        'requests',
        'openapi-spec-validator',
        'tenacity',
        'httpx'
    ],
    entry_points={
        'console_scripts': [
            'generate-client=api_client_generator.generator:main',
        ],
    },
)


from setuptools import find_packages, setup


def read(filename):
    with open(filename, "r") as file:
        return file.read()

setup(
    name="api-client-generator",
    version="1.0.0",
    packages=find_packages(),
    url="https://github.com/RadwanHegazy/pythonwebui",
    license="MIT",
    description="Build your HTML and CSS with ease",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Radwan Hegazy",
    python_requires=">=3.8",
    project_urls={
        "source": "https://github.com/RadwanHegazy/pythonwebui"
    }
)
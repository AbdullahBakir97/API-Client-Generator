from setuptools import find_packages, setup


def read(filename):
    with open(filename, "r") as file:
        return file.read()

setup(
    name="api-client-generator",
    version="1.0.0",
    packages=find_packages(),
    url="https://github.com/AbdullahBakir97/API-Client-Generator",
    license="MIT",
    description="A tool to automatically generate client libraries for RESTful APIs based on OpenAPI/Swagger specifications",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Radwan Hegazy",
    author_email="radwan.hegazy@example.com",
    python_requires=">=3.8",
    project_urls={
        "Documentation": "https://github.com/AbdullahBakir97/API-Client-Generator/wiki",
        "Source": "https://github.com/AbdullahBakir97/API-Client-Generator",
        "Bug Tracker": "https://github.com/AbdullahBakir97/API-Client-Generator/issues",
    },
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

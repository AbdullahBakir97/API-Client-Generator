# API Client Generator

## Overview
The API Client Generator is a Python library to automatically generate client libraries for RESTful APIs based on OpenAPI/Swagger specifications.

## Features
- Supports OpenAPI 3.0 specifications
- Generates client code for synchronous and asynchronous requests
- Handles authentication, pagination, and rate-limiting
- Customizable templates for different programming languages

## Installation

```bash
pip install api-client-generator
```

## Generating a Client


```python
from api_client_generator.generator import generate_client, load_openapi_spec

spec = load_openapi_spec('path/to/openapi.yaml')
generate_client(spec, output_dir='generated_client')
```

## Using the Generated Client Examples

```python
from generated_client.client import MyAPIClient

client = MyAPIClient(base_url='https://api.example.com', auth_token='your_token')
response = client.get_users()
print(response)
```



## Project Structure

api-client-generator/
├── api_client_generator/
│   ├── __init__.py
│   ├── generator.py
│   ├── templates/
│   │   ├── client.py.j2
│   │   ├── endpoint.py.j2
│   ├── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_generator.py
│   ├── petstore.yaml
│   ├── generated/
│   │   ├── client.py
├── examples/
│   ├── example_usage.py
├── docs/
│   ├── conf.py
│   ├── index.md
│   ├── tutorials/
│   │   ├── getting_started.md
├── README.md
├── setup.py
├── requirements.txt
├── .gitignore
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
└── CHANGELOG.md


## Contributing
We welcome contributions! Please see our Contribution Guidelines for more information.

## License
This project is licensed under the MIT License.
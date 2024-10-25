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



## Contributing
We welcome contributions! Please see our Contribution Guidelines for more information.

## License
This project is licensed under the MIT License.

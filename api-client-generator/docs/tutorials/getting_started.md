# API Client Generator

## Overview
The API Client Generator is a tool to automatically generate client libraries for RESTful APIs based on OpenAPI/Swagger specifications.

# Getting Started

This tutorial will guide you through setting up the API Client Generator and generating your first client library.

## Prerequisites
- Python 3.7 or higher
- OpenAPI/Swagger specification file

## Installation

```
pip install api-client-generator
```


## Generating a Client


```python
from api_client_generator.generator import generate_client, load_openapi_spec

spec = load_openapi_spec('path/to/openapi.yaml')
generate_client(spec, output_dir='generated_client')
```

## Using the Generated Client

```python
from generated_client.client import MyAPIClient

client = MyAPIClient(base_url='https://api.example.com', auth_token='your_token')
response = client.get_users()
print(response)
```
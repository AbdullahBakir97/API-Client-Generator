import pytest
from api_client_generator.generator import load_openapi_spec, generate_client

def test_load_openapi_spec():
    spec = load_openapi_spec('tests/petstore.yaml')
    assert spec['info']['title'] == 'Swagger Petstore'

def test_generate_client():
    spec = load_openapi_spec('tests/petstore.yaml')
    generate_client(spec, output_dir='tests/generated')
    with open('tests/generated/client.py', 'r') as file:
        client_code = file.read()
    assert 'class SwaggerPetstoreClient' in client_code

def test_generated_client():
    from tests.generated.client import SwaggerPetstoreClient

    client = SwaggerPetstoreClient(base_url='https://petstore.swagger.io/v2')
    pets = client.get_pet_findByStatus(status='available')
    assert len(pets) > 0

# api_client_generator/generator.py
import yaml
from openapi_spec_validator import validate_v3_spec
from jinja2 import Environment, FileSystemLoader
import logging
from tenacity import retry, stop_after_attempt, wait_exponential
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class APIClientError(Exception):
    pass

def load_openapi_spec(filepath):
    with open(filepath, 'r') as file:
        spec = yaml.safe_load(file)
    validate_v3_spec(spec)
    return spec

def render_template(template_name, context, custom_template_path=None):
    if custom_template_path:
        env = Environment(loader=FileSystemLoader(custom_template_path))
    else:
        env = Environment(loader=FileSystemLoader('api_client_generator/templates'))
    template = env.get_template(template_name)
    return template.render(context)

def generate_client(spec, output_dir='generated_client', custom_template_path=None):
    context = {
        'endpoints': spec['paths'],
        'components': spec['components'],
        'info': spec['info']
    }
    client_code = render_template('client.py.j2', context, custom_template_path)
    with open(f'{output_dir}/client.py', 'w') as file:
        file.write(client_code)

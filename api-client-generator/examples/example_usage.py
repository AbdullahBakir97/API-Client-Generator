from generated_client.client import SwaggerPetstoreClient

client = SwaggerPetstoreClient(base_url='https://petstore.swagger.io/v2', auth_token='your_token')
response = client.get_pet_findByStatus(status='available')
print(response)

import httpx
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AsyncAPIClient:
    def __init__(self, base_url, auth_token=None, timeout=30, headers=None):
        self.base_url = base_url
        self.auth_token = auth_token
        self.timeout = timeout
        self.headers = headers or {}
        self.client = httpx.AsyncClient()
        if self.auth_token:
            self.client.headers.update({'Authorization': f'Bearer {self.auth_token}'})
        self.client.headers.update(self.headers)

    async def request(self, method, url, **kwargs):
        logger.info(f"Making {method.upper()} request to {url}")
        try:
            response = await self.client.request(method, url, **kwargs)
            response.raise_for_status()
            logger.debug(f"Response: {response.json()}")
            return response.json()
        except httpx.RequestError as e:
            logger.error(f"Request failed: {e}")
            raise APIClientError(f"Request failed: {e}")

    async def close(self):
        await self.client.aclose()

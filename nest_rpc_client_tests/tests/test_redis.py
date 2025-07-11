import pytest
from nest_rpc_client.client import Client
from nest_rpc_client.config.redis import RedisConfig
from nest_rpc_client.transports.redis import RedisTransport


@pytest.mark.asyncio
async def test_redis_send():
    config = RedisConfig("localhost", 6379)
    transport = RedisTransport(config)
    client = Client(transport)

    async with client:
        response = await client.send("some", {"key": "value"})
        assert response["transport"] == "redis"
        assert response["payload"] == {"key": "value"}

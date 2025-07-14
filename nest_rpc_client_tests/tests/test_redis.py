import pytest
from nest_rpc_client.client import Client
from nest_rpc_client.config.redis import RedisConfig
from nest_rpc_client.transports.redis import RedisTransport
from nest_rpc_client.utils.parse_response import RpcException


@pytest.fixture
def client():
    config = RedisConfig("localhost", 6379)
    transport = RedisTransport(config)
    return Client(transport)


@pytest.mark.asyncio
async def test_redis_send(client: Client):
    async with client:
        response = await client.send("some", {"key": "value"})
        assert response["transport"] == "redis"
        assert response["payload"] == {"key": "value"}


@pytest.mark.asyncio
async def test_redis_emit(client: Client):
    async with client:
        response = await client.emit("event", {"some": "data to redis"})
        assert response is None

        sent_events = await client.send("get_events", {"transport": "redis"})
        assert len(sent_events) == 1
        assert sent_events[0]["payload"] == {"some": "data to redis"}

        await client.send("clear_events", {})


@pytest.mark.asyncio
async def test_redis_send_error(client: Client):
    async with client:
        with pytest.raises(RpcException) as e:
            await client.send(
                "send_error",
                {"send": "error payload"},
            )

        assert e.value.err == {
            "transport": "redis",
            "payload": {"send": "error payload"},
        }

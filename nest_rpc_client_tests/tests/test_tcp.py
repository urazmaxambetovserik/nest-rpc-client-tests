import pytest
from nest_rpc_client.client import Client
from nest_rpc_client.config.tcp import TCPConfig
from nest_rpc_client.exceptions.rpc import RpcException
from nest_rpc_client.transports.tcp import TCPTransport


@pytest.fixture
def client():
    config = TCPConfig("localhost", 3002)
    transport = TCPTransport(config)
    return Client(transport)


@pytest.mark.asyncio
async def test_tcp_send(client: Client):
    async with client:
        some_very_big_text = "some" * 100000
        response = await client.send("some", {"some": some_very_big_text})
        assert response["transport"] == "tcp"
        assert response["payload"] == {"some": some_very_big_text}


@pytest.mark.asyncio
async def test_tcp_emit(client: Client):
    async with client:
        response = await client.emit("event", {"some": "data to redis"})
        assert response is None

        sent_events = await client.send("get_events", {"transport": "tcp"})
        assert len(sent_events) == 1
        assert sent_events[0]["payload"] == {"some": "data to redis"}

        await client.send("clear_events", {})


@pytest.mark.asyncio
async def test_tcp_send_error(client: Client):
    async with client:
        with pytest.raises(RpcException) as e:
            await client.send(
                "send_error",
                {"send": "error payload"},
            )

        assert e.value.err == {
            "transport": "tcp",
            "payload": {"send": "error payload"},
        }

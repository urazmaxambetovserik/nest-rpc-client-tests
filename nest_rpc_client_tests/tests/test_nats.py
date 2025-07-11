import pytest
from nest_rpc_client.client import Client
from nest_rpc_client.config.nats import NATSConfig
from nest_rpc_client.transports.nats import NATSTransport


@pytest.fixture
def client():
    config = NATSConfig(["nats://localhost:4222"])
    transport = NATSTransport(config)
    return Client(transport)


@pytest.mark.asyncio
async def test_nats_send(client: Client):
    async with client:
        response = await client.send("some", {"key": "value"})
        assert response["transport"] == "nats"
        assert response["payload"] == {"key": "value"}


@pytest.mark.asyncio
async def test_nats_emit(client: Client):
    async with client:
        response = await client.emit("event", {"some": "data to nats"})
        assert response is None

        sent_events = await client.send("get_events", {"transport": "nats"})
        assert len(sent_events) == 1
        assert sent_events[0]["payload"] == {"some": "data to nats"}

        await client.send("clear_events", {})

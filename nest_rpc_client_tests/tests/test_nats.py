import pytest
from nest_rpc_client.client import Client
from nest_rpc_client.config.nats import NATSConfig
from nest_rpc_client.transports.nats import NATSTransport


@pytest.mark.asyncio
async def test_nats_send():
    config = NATSConfig(["nats://localhost:4222"])
    transport = NATSTransport(config)
    client = Client(transport)

    async with client:
        response = await client.send("some", {"key": "value"})
        assert response["transport"] == "nats"
        assert response["payload"] == {"key": "value"}

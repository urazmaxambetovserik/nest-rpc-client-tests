import pytest
from nest_rpc_client.client import Client
from nest_rpc_client.config.rabbitmq import RabbitMQConfig
from nest_rpc_client.transports.rabbitmq import RabbitMQTransport


@pytest.fixture
def client():
    config = RabbitMQConfig("amqp://localhost:5672", "rmq")
    transport = RabbitMQTransport(config)
    return Client(transport)


@pytest.mark.asyncio
async def test_rabbitmq_send(client: Client):
    async with client:
        response = await client.send("some", {"key": "value"})
        assert response["transport"] == "rmq"
        assert response["payload"] == {"key": "value"}


@pytest.mark.asyncio
async def test_rabbitmq_emit(client: Client):
    async with client:
        response = await client.emit("event", {"some": "value to rmq"})
        assert response is None

        sent_events = await client.send("get_events", {"transport": "rmq"})
        assert len(sent_events) == 1
        assert sent_events[0]["payload"] == {"some": "value to rmq"}

        await client.send("clear_events", {})

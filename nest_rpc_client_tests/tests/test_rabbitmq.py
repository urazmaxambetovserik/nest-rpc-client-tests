import pytest
from nest_rpc_client.client import Client
from nest_rpc_client.config.rabbitmq import RabbitMQConfig
from nest_rpc_client.transports.rabbitmq import RabbitMQTransport


@pytest.mark.asyncio
async def test_rabbitmq_send():
    config = RabbitMQConfig("amqp://localhost:5672", "rmq")
    transport = RabbitMQTransport(config)
    client = Client(transport)

    async with client:
        response = await transport.send("some", {"key": "value"})
        assert response["transport"] == "rmq"
        assert response["payload"] == {"key": "value"}

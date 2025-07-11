# nest-rpc-client-tests

Integration and system tests for [nest-rpc-client](https://github.com/urazmaxambetovserik/nest-rpc-client).

This repository is designed to validate that the **nest-rpc-client** Python package can interoperate correctly with NestJS microservices over different transports (RabbitMQ, Redis, NATS, etc.).

## Running Tests

```bash
cd nest_rpc_client_tests
python3 -m venv venv
source venv/bin/activate
pip install -r requiremenets.txt

# Start the brokers:
docker-compose -f docker-compose.test.yml up -d
# Or
docker compose -f docker-compose.test.yml up -d # (Unix)

pytest
```

## Related

[nest-rpc-client](https://pypi.org/project/nest-rpc-client/) - The Python client library being tested.

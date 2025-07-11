import { NestFactory } from '@nestjs/core';
import { MicroserviceOptions, Transport } from '@nestjs/microservices';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  app.connectMicroservice<MicroserviceOptions>({
    transport: Transport.RMQ,
    options: { urls: ['amqp://localhost:5672'] },
  });

  app.connectMicroservice<MicroserviceOptions>({
    transport: Transport.REDIS,
    options: { host: 'localhost', port: 6379 },
  });

  app.connectMicroservice<MicroserviceOptions>({
    transport: Transport.NATS,
    options: { servers: ['nats://localhost:4222'] },
  });

  await app.listen(process.env.PORT ?? 3000);
}

bootstrap();

import { Controller } from '@nestjs/common';
import { MessagePattern, Payload, Transport } from '@nestjs/microservices';

@Controller()
export class AppController {
  @MessagePattern('some', Transport.NATS)
  natsSome(@Payload() payload: object) {
    return { transport: 'nats', payload };
  }

  @MessagePattern('some', Transport.REDIS)
  redisSome(@Payload() payload: object) {
    return { transport: 'redis', payload };
  }

  @MessagePattern('some', Transport.RMQ)
  rmqSome(@Payload() payload: object) {
    return { transport: 'rmq', payload };
  }
}

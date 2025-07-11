import { Controller } from '@nestjs/common';
import {
  EventPattern,
  MessagePattern,
  Payload,
  Transport,
} from '@nestjs/microservices';

@Controller()
export class AppController {
  private events: { transport: string; payload: object }[] = [];

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

  @EventPattern('event', Transport.NATS)
  natsEvent(@Payload() payload: object) {
    this.events.push({ transport: 'nats', payload });
  }

  @EventPattern('event', Transport.REDIS)
  redisEvent(@Payload() payload: object) {
    this.events.push({ transport: 'redis', payload });
  }

  @EventPattern('event', Transport.RMQ)
  rmqEvent(@Payload() payload: object) {
    this.events.push({ transport: 'rmq', payload });
  }

  // For test events
  @MessagePattern('clear_events')
  clearEvents() {
    this.events = [];
    return {};
  }

  @MessagePattern('get_events')
  getEvents(@Payload() payload: { transport: string }) {
    return this.events.filter((e) => e.transport === payload.transport);
  }
}

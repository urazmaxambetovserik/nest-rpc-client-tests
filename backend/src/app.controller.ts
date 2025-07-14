import { Controller, UseFilters } from '@nestjs/common';
import {
  EventPattern,
  MessagePattern,
  Payload,
  RpcException,
  Transport,
} from '@nestjs/microservices';
import { AppExceptionFilter } from './app-exception.filter';

@UseFilters(new AppExceptionFilter())
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

  @MessagePattern('some', Transport.TCP)
  tcpSome(@Payload() payload: object) {
    return { transport: 'tcp', payload };
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

  @EventPattern('event', Transport.TCP)
  tcpEvent(@Payload() payload: object) {
    this.events.push({ transport: 'tcp', payload });
  }

  @MessagePattern('send_error', Transport.NATS)
  natsSendError(@Payload() payload: object) {
    throw new RpcException({ transport: 'nats', payload });
  }

  @MessagePattern('send_error', Transport.REDIS)
  redisSendError(@Payload() payload: object) {
    console.log('redis err');
    console.log(payload);
    throw new RpcException({ transport: 'redis', payload });
  }

  @MessagePattern('send_error', Transport.RMQ)
  rmqSendError(@Payload() payload: object) {
    throw new RpcException({ transport: 'rmq', payload });
  }

  @MessagePattern('send_error', Transport.TCP)
  tcpSendError(@Payload() payload: object) {
    throw new RpcException({ transport: 'tcp', payload });
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

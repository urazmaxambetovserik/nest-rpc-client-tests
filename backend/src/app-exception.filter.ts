import { ArgumentsHost, Catch, RpcExceptionFilter } from '@nestjs/common';
import { RpcException } from '@nestjs/microservices';
import { Observable, throwError } from 'rxjs';

@Catch(RpcException)
export class AppExceptionFilter implements RpcExceptionFilter<RpcException> {
  catch(exception: RpcException, _: ArgumentsHost): Observable<any> {
    console.log(exception);
    return throwError(() => exception.getError());
  }
}

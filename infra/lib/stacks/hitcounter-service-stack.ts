import * as cdk from '@aws-cdk/core'
import * as apigwv2 from '@aws-cdk/aws-apigatewayv2'
import { HitCounterService } from '../constructs/services/hitcounter'
import { IHttpApi2 } from '../interfaces/interface'

interface Props extends cdk.StackProps {
  api: IHttpApi2
}

export class HitcounterServiceStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props: Props) {
    super(scope, id, props)

    const service = new HitCounterService(this, `HitCounterService`)
    props.api.addRoute({
      scope: this,
      routeId: `GetCount`,
      path: '/{proxy+}',
      method: apigwv2.HttpMethod.GET,
      handler: service.getCount,
    })
    props.api.addRoute({
      scope: this,
      routeId: `UpdateCount`,
      path: '/{proxy+}',
      method: apigwv2.HttpMethod.POST,
      handler: service.updateCount,
    })
  }

}

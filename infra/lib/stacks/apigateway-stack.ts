import * as cdk from '@aws-cdk/core'
import { HttpApi } from '../constructs/httpapi'
import { IHttpApi2 } from '../interfaces/interface'

interface Props extends cdk.StackProps {
  userPoolId: string
  userPoolClientId: string
}

export class ApiGatewayStack extends cdk.Stack {
  public readonly api: IHttpApi2

  constructor(scope: cdk.Construct, id: string, props: Props) {
    super(scope, id, props)

    const ns = this.node.tryGetContext('ns')

    const httpApi = new HttpApi(this, `HttpApi`, {
      userPoolId: props.userPoolId,
      userPoolClientId: props.userPoolClientId,
    })
    this.api = httpApi

    new cdk.CfnOutput(this, `HttpApiUrl`, {
      exportName: `${ns}HttpApiUrl`,
      value: `${httpApi.api.defaultStage!.url}` || 'undefined',
    })
  }

}

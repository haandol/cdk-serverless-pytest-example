import * as cdk from '@aws-cdk/core'
import * as apigwv2 from '@aws-cdk/aws-apigatewayv2'
import * as integrations from '@aws-cdk/aws-apigatewayv2-integrations'
import { IHttpApi2, IRouteProps } from '../interfaces/interface'

interface IProps {
  userPoolId: string
  userPoolClientId: string
}

export class HttpApi extends cdk.Construct implements IHttpApi2 {
  public readonly api: apigwv2.HttpApi
  public readonly authorizer: apigwv2.IHttpRouteAuthorizer

  constructor(scope: cdk.Construct, id: string, props: IProps) {
    super(scope, id)

    this.api = this.createHttpApi()
    this.authorizer = this.createJWTAuthorizer(this.api, props)
  }

  public addRoute(props: IRouteProps) {
    const routeKey = props.path ? apigwv2.HttpRouteKey.with(props.path, props.method) : apigwv2.HttpRouteKey.DEFAULT
    const authorizer = props.authorize ? this.authorizer : new apigwv2.HttpNoneAuthorizer()
    const integration = new integrations.LambdaProxyIntegration({ handler: props.handler })
    return new apigwv2.HttpRoute(this, `${props.routeId}Route`, {
      httpApi: this.api,
      routeKey,
      authorizer,
      integration,
    })
  }

  private createHttpApi(): apigwv2.HttpApi {
    const ns = this.node.tryGetContext('ns')
    return new apigwv2.HttpApi(this, 'HttpApi', {
      apiName: `${ns}HttpApi`,
      corsPreflight: {
        allowHeaders: ['*'],
        allowMethods: [apigwv2.CorsHttpMethod.ANY],
        allowOrigins: ['*'],
        maxAge: cdk.Duration.seconds(0),
      },
      createDefaultStage: true,
    })
  }

  private createJWTAuthorizer(httpApi: apigwv2.IHttpApi, props: IProps): apigwv2.IHttpRouteAuthorizer {
    const ns = this.node.tryGetContext('ns')
    const region = cdk.Stack.of(this).region

    const authorizer = new apigwv2.HttpAuthorizer(this, `JWTAuthorizer`, {
      authorizerName: `${ns}JWTAuthorizer`,
      httpApi,
      type: apigwv2.HttpAuthorizerType.JWT,
      identitySource: ['$request.header.Authorization'],
      jwtAudience: [props.userPoolClientId],
      jwtIssuer: `https://cognito-idp.${region}.amazonaws.com/${props.userPoolId}`,
    })
    return apigwv2.HttpAuthorizer.fromHttpAuthorizerAttributes(this, `JWTRouteAuthorizer`, {
      authorizerId: authorizer.authorizerId,
      authorizerType: apigwv2.HttpAuthorizerType.JWT,
    })
  }

}

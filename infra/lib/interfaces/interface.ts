import * as cdk from '@aws-cdk/core'
import * as lambda from '@aws-cdk/aws-lambda'
import * as apigwv2 from '@aws-cdk/aws-apigatewayv2'

export interface IRouteProps {
  scope?: cdk.Construct
  authorize?: boolean
  path?: string
  routeId: string
  method: apigwv2.HttpMethod
  handler: lambda.IFunction
}

export interface IHttpApi2 {
  api: apigwv2.IHttpApi
  authorizer?: apigwv2.IHttpRouteAuthorizer
  addRoute: (props: IRouteProps) => apigwv2.IHttpRoute
}
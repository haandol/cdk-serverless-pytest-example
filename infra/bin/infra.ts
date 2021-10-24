#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from '@aws-cdk/core';
import { AuthStack } from '../lib/stacks/auth-stack'
import { ApiGatewayStack } from '../lib/stacks/apigateway-stack'
import { StorageStack } from '../lib/stacks/storage-stack'
import { HitcounterServiceStack } from '../lib/stacks/hitcounter-service-stack'
import { App } from '../lib/constants/config'

const ns = App.ns
const app = new cdk.App({
  context: { ns },
})

new StorageStack(app, `${ns}StorageStack`)

const auth = new AuthStack(app, `${ns}AuthStack`)

const apiGateway = new ApiGatewayStack(app, `${ns}ApiGatewayStack`, {
  userPoolId: auth.userPool.userPoolId,
  userPoolClientId: auth.userPoolClient.userPoolClientId,
})
apiGateway.addDependency(auth)

new HitcounterServiceStack(app, `${ns}HitcounterServiceStack`, {
  api: apiGateway.api,
})
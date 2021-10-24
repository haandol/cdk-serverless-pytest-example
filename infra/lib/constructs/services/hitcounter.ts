import * as path from 'path'
import * as cdk from '@aws-cdk/core'
import * as iam from '@aws-cdk/aws-iam'
import * as lambda from '@aws-cdk/aws-lambda'
import * as lambdaPython from '@aws-cdk/aws-lambda-python'
import { Table } from '../../constants/config'

export class HitCounterService extends cdk.Construct {
  public readonly getCount: lambda.IFunction
  public readonly updateCount: lambda.IFunction

  constructor(scope: cdk.Construct, id: string) {
    super(scope, id)

    const ns = this.node.tryGetContext('ns')

    this.updateCount = new lambdaPython.PythonFunction(this, `UpdateCount`, {
      functionName: `${ns}UpdateCount`,
      entry: path.resolve(__dirname, '..', '..', 'functions', 'services', 'hitcounter', 'update'),
      runtime: lambda.Runtime.PYTHON_3_8,
      environment: {
        TABLE_NAME: Table.Name,
      },
    })
    this.updateCount.addToRolePolicy(new iam.PolicyStatement({
      actions: Table.Actions.ReadWrite,
      resources: Table.getResources(this),
    }))

    this.getCount = new lambdaPython.PythonFunction(this, `GetCount`, {
      functionName: `${ns}GetCount`,
      entry: path.resolve(__dirname, '..', '..', 'functions', 'services', 'hitcounter', 'get'),
      runtime: lambda.Runtime.PYTHON_3_8,
      environment: {
        TABLE_NAME: Table.Name,
      },
    })
    this.getCount.addToRolePolicy(new iam.PolicyStatement({
      actions: Table.Actions.Read,
      resources: Table.getResources(this),
    }))
 
  }

}
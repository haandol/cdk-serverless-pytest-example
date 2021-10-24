import * as path from 'path'
import * as cdk from '@aws-cdk/core';
import * as lambda from '@aws-cdk/aws-lambda'
import * as dynamodb from '@aws-cdk/aws-dynamodb'
import * as lambdaPython from '@aws-cdk/aws-lambda-python'

export class InfraStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const table = this.createMainTable()
    this.createHitCounterFunction(table)

  }

  private createMainTable() {
    const ns = this.node.tryGetContext('ns')
    return new dynamodb.Table(this, `MainTable`, {
      tableName: `${ns}Main`,
      partitionKey: {
        name: 'PK',
        type: dynamodb.AttributeType.STRING,
      },
      sortKey: {
        name: 'SK',
        type: dynamodb.AttributeType.STRING,
      },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      encryption: dynamodb.TableEncryption.AWS_MANAGED,
    })
  }

  private createHitCounterFunction(table: dynamodb.ITable) {
    const fn = new lambdaPython.PythonFunction(this, `HitCounterFunction`, {
      entry: path.resolve(__dirname, '..', 'functions', 'hitcounter'),
      index: 'index.py',
      handler: 'handler',
      runtime: lambda.Runtime.PYTHON_3_8,
      environment: {
        TABLE: table.tableName,
      },
    })
    table.grantReadWriteData(fn)
  }

}

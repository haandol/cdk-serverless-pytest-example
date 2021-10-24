import * as cdk from '@aws-cdk/core'

export namespace App {
  export const ns = 'CdkSlsPytest'
}

export namespace IdentityProvider {
  export const RedirectUri = 'http://localhost:3000'
}

export namespace Table {
  export const Name = `${App.ns}Main`

  export const getResources = (scope: cdk.Construct) => {
    return [
      `arn:aws:dynamodb:${cdk.Stack.of(scope).region}:${cdk.Stack.of(scope).account}:table/${Table.Name}`,
      `arn:aws:dynamodb:${cdk.Stack.of(scope).region}:${cdk.Stack.of(scope).account}:table/${Table.Name}/*`
    ]
  }

  export const Actions = {
    Read: [
      'dynamodb:BatchGetItem',
      'dynamodb:Get*',
      'dynamodb:Query',
      'dynamodb:Scan',
    ],
    ReadWrite: [
      'dynamodb:BatchGetItem',
      'dynamodb:GetItem',
      'dynamodb:GetRecords',
      'dynamodb:GetShardIterator',
      'dynamodb:Query',
      'dynamodb:Scan',
      'dynamodb:BatchWriteItem',
      'dynamodb:DeleteItem',
      'dynamodb:PutItem',
      'dynamodb:UpdateItem',
    ],
  }
}

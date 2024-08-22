# Deployment Template 1

This is my personal template for code deployment. Not all 
services need to run like this, but I find it handy for 
certain situations.

# Environment variables that are required to be defined in the GitHub

## Add these to the repository secrets
+ __AWS_ACCOUNT_ID__: example: 123456789000 
+ __GHA_ASSUMED_ROLE__: example: arn:aws:iam::******:role/RoleName

# What to set up in ECR

Follow [these](docs/AWS-ECR-setup.md) instructions to create a repository for images in ECR.

# Create an app using AWS Copilot

```shell
$ copilot app init
```

```shell
$ copilot init
```

```shell
$ copilot job run
```

Run the following command after making changes in a manifest file
```shell
$ copilot deploy
```

# TODO

+ When creating a job using copilot I use special IAM user created for that. 
  But that user has more privileges than it should. 
  The next step is to reduce user's privileges to only
  those that are necessary to create an infrastructure.

# Resources

## Setting Up OIDC:
+ https://aws.amazon.com/blogs/security/use-iam-roles-to-connect-github-actions-to-actions-in-aws/
+ https://github.com/aws-actions/configure-aws-credentials
+ https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect
+ https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services

## Building docker image
+ https://github.com/docker/build-push-action
+ https://github.com/marketplace/actions/build-and-push-docker-images
+ https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-and-push-docker-images-to-amazon-ecr-using-github-actions-and-terraform.html

## ECR polices 
+ https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policy-examples.html

## ECS
+ https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html

## AWS Copilot
+ https://aws.github.io/copilot-cli/docs/overview/
+ 



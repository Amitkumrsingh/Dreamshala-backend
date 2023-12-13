# Dshala Backend project

In this project, we are using django as the backend framework and postgresql as the backend database.

# How to create AWS CI/CD pipeline

# Django CI/CD Pipeline in AWS

## Why CI/CD?

Continuous Integration and Continuous Deployment offer several benefits:

- **Speed and Efficiency**: Automate processes to release new features and bug fixes quickly.
- **Reliability**: Identify and fix errors early in development to ensure high-quality software.
- **Collaboration**: Facilitate teamwork by integrating code changes into a shared repository.
- **Continuous Feedback**: Receive quick feedback through continuous testing and deployment.
- **Enhanced Security**: Detect and address security vulnerabilities promptly.

## Setting Up the CI/CD Pipeline

Follow these steps to implement the CI/CD pipeline in AWS:

### 1. Create a New IAM Role

- Log in to your AWS account.
- Navigate to IAM in the AWS Management Console.
- Create a new IAM role with permissions for services such as CodeDeploy and S3 access.

### 2. Create an EC2 Instance

- Launch an EC2 instance using the Ubuntu 20.04 or 20.10 image.
- Configure instance settings, including security options and key pairs.

### 3. Install CodeDeploy-Agent on the Server

- Connect to your server and update repositories.
- Install necessary packages: `sudo apt install ruby-full` and `sudo apt install wget`.
- Download and install the CodeDeploy-Agent.
- Verify the installation status: `sudo service codedeploy-agent status`.

### 4. Set Up Configuration Files

Create two crucial configuration files in the root directory of your GitHub repository:

- `buildspec.yml`: Contains build configurations for AWS CodeBuild.
- `appspec.yml`: Contains deployment configurations for AWS CodeDeploy.

### 5. Create a CodePipeline

- In the AWS Management Console, navigate to CodePipeline.
- Create a new build project in CodeBuild, specifying source, environment, buildspec file, and log preferences.
- Create a CodeDeploy application and deployment group.
- Create a CodePipeline, connecting GitHub as the source and integrating CodeBuild and CodeDeploy for build and deployment stages.

This automated pipeline triggers a release, cloning the repository, running tests, and deploying the application to the server.

## Getting Started

To follow this tutorial, ensure you have:

- An AWS account

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



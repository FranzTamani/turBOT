# HOW TO USE

### Install Terraform
Before proceeding, please configure the Terraform CLI through:  https://learn.hashicorp.com/tutorials/terraform/install-cli

### Export the following environment variables using the details given on the AWS account

```
export AWS_ACCESS_KEY_ID="anaccesskey"
export AWS_SECRET_ACCESS_KEY="asecretkey"
export AWS_SESSION_TOKEN="asessiontoken"
```

### Managing the Infrastructure
Navigate to "testing-infra" folder and run the following:

```
terraform init
```
The terraform init command will download all the dependecies required to deploy the infrastructure to AWS.
NOTE: YOU MUST CREATE A KEY PAIR INSIDE THE AWS CONSOLE TO REFERENCE HERE.

```
terraform plan \
-var "instance_name=test-instance" \
-var "key_name=test" \
-out=tf.plan
```
The terraform plan command will plan the deployment of the infrastructure and show the user any changes being made in AWS.

```
terraform apply tf.plan
```
The terraform apply command will apply the changes outline in the terraform plan command.

```
terraform destroy \
-var "instance_name=test-instance" \
-var "key_name=test"
```
The terraform destroy command will take down all of the infrastructure deployed by the terraform apply command.

# Troubleshooting
If "Unprotected" or "Too Open" error occurs during SSH. Update the user permissions to only allow a single specific user.
On linux specify "chmod 400 keyfile.pem"

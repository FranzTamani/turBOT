# HOW TO USE

### Export the following environment variables using the details given on the AWS account

export AWS_ACCESS_KEY_ID="anaccesskey"
export AWS_SECRET_ACCESS_KEY="asecretkey"
export AWS_SESSION_TOKEN="asessiontoken"

### Managing the Infrastructure
Navigate to "testing-infra" folder and run the following:

```
terraform plan \
-var "instance_name=test-instance" \
-out=tf.plan
```
The terraform plan command will plan the deployment of the infrastructure and show the user any changes being made in AWS.

```
terraform apply tf.plan
```
The terraform apply command will apply the changes outline in the terraform plan command.

```
terraform destroy \
-var "instance_name=test-instance"
```
The terraform destroy command will take down all of the infrastructure deployed by the terraform apply command.
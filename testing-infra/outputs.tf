output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.instance.public_ip
}
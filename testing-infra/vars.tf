variable "instance_name" {
  type        = string
  description = "The desired name for the EC2 Instance"
}

variable "key_name" {
  type        = string
  description = "The desired name for the EC2 Instance"
  default     = "test"
}

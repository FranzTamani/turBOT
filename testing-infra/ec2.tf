data "aws_ami" "amazon-linux-2" {
  most_recent = true

  filter {
    name   = "owner-alias"
    values = ["amazon"]
  }

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm*"]
  }
}

data "template_file" "user_data" {
  template = file("${path.module}/user_data.txt")
}

resource "aws_instance" "instance" {
  launch_template = aws_launch_template.template.arn
  tags = {
    Name = var.instance_name
  }
}

resource "aws_launch_template" "template" {
  name = "${var.instance_name}-launch-template"

  block_device_mappings {
    device_name = "/dev/sda1"

    ebs {
      volume_size = 10
    }
  }

  image_id        = data.aws_ami.amazon-linux-2.id
  security_groups = [aws_security_group.allow_ssh]
  key_name        = var.key_name
  user_data       = filebase64("${path.module}/user_data.sh")
}

resource "aws_security_group" "allow_ssh" {
  name        = "Allow SSH"
  description = "Allow SSH inbound traffic"

  ingress = [
    {
      description = "Allow SSH Access"
      from_port   = 22
      to_port     = 22
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  ]

  egress = [
    {
      from_port   = 0
      to_port     = 0
      protocol    = "-1"
      cidr_blocks = ["0.0.0.0/0"]
    }
  ]
}
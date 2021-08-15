data "aws_ami" "amazon-linux-2" {
  most_recent = true
  owners      = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04*"]
  }
}

resource "aws_instance" "instance" {
  launch_template {
    id      = aws_launch_template.template.id
    version = "$Latest"
  }
  tags = {
    Name = var.instance_name
  }
}

resource "aws_launch_template" "template" {
  name = "${var.instance_name}-launch-template"

  network_interfaces {
    associate_public_ip_address = true
    security_groups             = [aws_security_group.allow_ssh.id]
  }

  instance_type = "t2.micro"
  image_id      = data.aws_ami.amazon-linux-2.id
  key_name      = var.key_name
  user_data     = filebase64("${path.module}/user_data.sh")
}

resource "aws_security_group" "allow_ssh" {
  name        = "Allow SSH"
  description = "Allow SSH inbound traffic"
}

resource "aws_security_group_rule" "example" {
  type              = "ingress"
  from_port         = 22
  to_port           = 22
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.allow_ssh.id
}

resource "aws_security_group_rule" "allow_all" {
  type              = "egress"
  to_port           = 0
  protocol          = "-1"
  from_port         = 0
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.allow_ssh.id
}
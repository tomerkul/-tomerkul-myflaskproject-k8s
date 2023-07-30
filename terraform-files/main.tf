provider "aws" {
  region = "us-east-1"
}

variable "existing_key_name" {
  default = "mykeyVir"
}


resource "aws_instance" "example" {
  ami           = "ami-0f34c5ae932e6f0e4"
  instance_type = "t2.micro"
  key_name      = var.existing_key_name  # Use the existing key pair

  tags = {
    Name = "Example EC2 Instance"
  }


  vpc_security_group_ids = ["launch-wizard-1"]


  connection {
    type        = "ssh"
    user        = "ec2-user"          # The username for the SSH connection (varies based on the AMI)
    private_key = file("~/.ssh/id_rsa")  # Path to the private key file on your local machine
    host        = self.public_ip      # This will automatically get the public IP of the instance
  }
}



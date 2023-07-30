provider "aws" {
  region = "us-east-2"
}


resource "aws_instance" "example" {
  ami           = "ami-02a89066c48741345"
  instance_type = "t2.micro"
  key_name      = "tst"
  vpc_security_group_ids = [aws_security_group.instance.id]

  tags = {
    Name = "Example Instance"
  }

  connection {
      type        = "ssh"
      user        = "ec2-user"  # The SSH user for the AMI you are using (Amazon Linux uses "ec2-user")
      private_key = file("~/.ssh/tst.pem")
      host        = self.public_ip  # The public IP of the EC2 instance
    }

  provisioner "remote-exec" {
     inline = [
       "sudo yum update -y",
       "sudo yum install -y nginx",
       "sudo systemctl start nginx",
       "sudo systemctl enable nginx",
     ]
  }

}

resource "aws_security_group" "instance" {
  name = "terraform-example-instance"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"  # All protocols
    cidr_blocks     = ["10.0.0.0/16"]  # Replace with your desired destination IP range
  }
}

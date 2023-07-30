provider "aws" {
  region = "us-east-1"
}

variable "existing_key_name" {
  default = "mykeyVir"
}


resource "aws_instance" "example" {
  ami           = "ami-0f34c5ae932e6f0e4"
  instance_type = "t2.micro"
  key_name      = var.existing_key_name  

  tags = {
    Name = "Example EC2 Instance"
  }


  vpc_security_group_ids = ["launch-wizard-1"]


  connection {
    type        = "ssh"
    user        = "ec2-user"          
    private_key = file("~/.ssh/id_rsa")  
    host        = self.public_ip      
  }
}



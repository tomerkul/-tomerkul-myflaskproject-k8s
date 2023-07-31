provider "aws" {
  region = "us-east-2"
}

data "aws_security_group" "existing" {
  name = "main"
}

resource "aws_instance" "example" {
  ami           = "ami-02a89066c48741345"
  instance_type = "t2.micro"
  key_name      = "tst"
  vpc_security_group_ids = [data.aws_security_group.existing.id]

  associate_public_ip_address = true

  tags = {
    Name = "Example Instance"
  }

  connection {
    type        = "ssh"
    user        = "ec2-user"
    private_key = file("~/.ssh/tst.pem")
    host        = self.public_ip
  }

  provisioner "file" {
    source      = "docker-compose.yaml"  # Relative path to docker-compose.yaml
    destination = "/home/ec2-user/docker-compose.yaml"
  }

  provisioner "file" {
    source      = "setup.sh"
    destination = "/tmp/setup.sh"
  }

  provisioner "remote-exec" {
    inline = [
      "chmod +x /tmp/setup.sh",
      "sudo /tmp/setup.sh",
    ]
  }

  provisioner "file" {
    source      = "flask_run.sh"
    destination = "/tmp/flask_run.sh"
  }

  provisioner "remote-exec" {
    inline = [
      "chmod +x /tmp/flask_run.sh",
      "sudo /tmp/flask_run.sh",
    ]
  }
}

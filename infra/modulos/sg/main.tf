resource "aws_security_group" "this" {
    vpc_id = var.vpc_id

    ingress  {
        from_port   = var.port_dev
        to_port     = var.port_dev
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
        from_port   = var.port_prod
        to_port     = var.port_prod
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    egress {
        from_port   = 0
        to_port     = 0
        protocol    = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }


  
}
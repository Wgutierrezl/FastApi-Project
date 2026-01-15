resource "aws_vpc" "this" {
    cidr_block = var.vpc_cidr
}

resource "aws_internet_gateway" "igw" {
    vpc_id = aws_vpc.this.id
}

resource "aws_subnet" "public" {
    count = 3
    vpc_id = aws_vpc.this.id
    cidr_block = var.public_subnet_cidr[count.index]
    availability_zone = element(
        ["us-east-1a", "us-east-1b", "us-east-1c"],count.index
    )
    map_public_ip_on_launch = true
}

resource "aws_route_table" "public" {
    vpc_id = aws_vpc.this.id

    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = aws_internet_gateway.igw.id
    }
}

resource "aws_route_table_association" "public" {
    count = 3
    subnet_id = aws_subnet.public[count.index].id
    route_table_id = aws_route_table.public.id
}
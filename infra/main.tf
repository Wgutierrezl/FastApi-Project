terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# 🔹 ECR
module "ecr" {
  source = "./modulos/ecr"
  ecr_repo_name_dev = "fastapi-repo_dev"
  ecr_repo_name_prod = "fastapi-repo_prod"
}

# 🔹 VPC
module "vpc" {
  source = "./modulos/vpc"

  vpc_cidr = "10.0.0.0/16"
  public_subnet_cidr = [
    "10.0.1.0/24",
    "10.0.2.0/24",
    "10.0.3.0/24"
  ]
}

# 🔹 Security Group
module "sg" {
  source = "./modulos/sg"
  vpc_id = module.vpc.vpc_id
  port_dev = 8071
  port_prod = 8072
}

# 🔹 ECS
module "ecs" {
  source = "./modulos/ecs"

  ecs_cluster_name  = "fastapi-cluster"
  service_name_dev  = "fastapi-service-dev"
  service_name_prod = "fastapi-service-prod"
  task_family_dev   = "fastapi-task-family-dev"
  task_family_prod  = "fastapi-task-family-prod"
  container_image_dev   = module.ecr.repository_url_dev
  container_image_prod  = module.ecr.repository_url_prod
  container_port_dev = 8071
  container_port_prod = 8072
  subnets_id        = module.vpc.subnet_ids
  security_group_id = module.sg.security_group_id
}

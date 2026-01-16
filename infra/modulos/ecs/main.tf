resource "aws_ecs_cluster" "this" {
  name = var.ecs_cluster_name

}

resource "aws_ecs_task_definition" "this_dev" {
    family = var.task_family_dev
    network_mode = "awsvpc"
    requires_compatibilities = ["FARGATE"]
    cpu = "256"
    memory = "512"
    execution_role_arn = "arn:aws:iam::723595585168:role/ecsTaskExecutionRole"
    container_definitions = jsonencode([
    {
      name  = "fastapi"
      image = var.container_image_dev
      portMappings = [
        {
          containerPort = var.container_port_dev
          hostPort      = var.container_port_dev
        }
      ]
    }
  ])
}

resource "aws_ecs_task_definition" "this_prod" {
  family = var.task_family_prod
  network_mode = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu = "256"
  memory = "512"
  execution_role_arn = "arn:aws:iam::723595585168:role/ecsTaskExecutionRole"

  container_definitions = jsonencode([
    {
      name  = "fastapi"
      image = var.container_image_prod
      portMappings = [
        {
          containerPort = var.container_port_prod
          hostPort      = var.container_port_prod
        }
      ]
    }
  ])
}

resource "aws_ecs_service" "this_dev" {
    name = var.service_name_dev
    cluster = aws_ecs_cluster.this.id
    task_definition = aws_ecs_task_definition.this_dev.arn
    desired_count = 1
    launch_type = "FARGATE"

    network_configuration {
      subnets = var.subnets_id
      security_groups = [var.security_group_id]
      assign_public_ip = true
    }
}

resource "aws_ecs_service" "this_prod" {
  name = var.service_name_prod
  cluster = aws_ecs_cluster.this.id
  task_definition = aws_ecs_task_definition.this_prod.arn
  desired_count = 1
  launch_type = "FARGATE"

  network_configuration {
    subnets = var.subnets_id
    security_groups = [var.security_group_id]
    assign_public_ip = true
  }
  
}
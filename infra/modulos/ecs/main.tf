resource "aws_ecs_cluster" "this" {
  name = var.ecs_cluster_name

}

resource "aws_ecs_task_definition" "this" {
    family = var.task_family
    network_mode = "awsvpc"
    requires_compatibilities = ["FARGATE"]
    cpu = "256"
    memory = "512"
    execution_role_arn = "arn:aws:iam::723595585168:role/ecsTaskExecutionRole"
    container_definitions = jsonencode([
    {
      name  = "fastapi"
      image = var.container_image
      portMappings = [
        {
          containerPort = var.container_port
          hostPort      = var.container_port
        }
      ]
    }
  ])
}

resource "aws_ecs_service" "this" {
    name = var.service_name
    cluster = aws_ecs_cluster.this.id
    task_definition = aws_ecs_task_definition.this.arn
    desired_count = 1
    launch_type = "FARGATE"

    network_configuration {
      subnets = var.subnets_id
      security_groups = [var.security_group_id]
      assign_public_ip = true

    }
  
}
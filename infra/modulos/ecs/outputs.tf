output "cluster_id" {
  description = "ID del ECS Cluster"
  value       = aws_ecs_cluster.this.id
}

output "service_name_dev" {
  description = "Nombre del ECS Service"
  value       = aws_ecs_service.this_dev.name
}

output "service_name_prod" {
  description = "Nombre del ECS Service"
  value       = aws_ecs_service.this_prod.name
}

output "task_definition_arn_dev" {
  description = "ARN de la Task Definition"
  value       = aws_ecs_task_definition.this_dev.arn
}

output "task_definition_arn_prod" {
  description = "ARN de la Task Definition"
  value       = aws_ecs_task_definition.this_prod.arn
}

output "cluster_id" {
  description = "ID del ECS Cluster"
  value       = aws_ecs_cluster.this.id
}

output "service_name" {
  description = "Nombre del ECS Service"
  value       = aws_ecs_service.this.name
}

output "task_definition_arn" {
  description = "ARN de la Task Definition"
  value       = aws_ecs_task_definition.this.arn
}

output "repository_url_dev" {
    description = "The URL of the ECR repository"
    value       = aws_ecr_repository.this_dev.repository_url
}

output "repository_url_prod" {
    description = "The URL of the ECR repository"
    value       = aws_ecr_repository.this_prod.repository_url
}
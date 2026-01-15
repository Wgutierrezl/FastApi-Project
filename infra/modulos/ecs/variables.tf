variable "ecs_cluster_name" {
    type = string
}
variable "service_name" {
    type = string
}
variable "task_family" {
    type = string
}
variable "container_image" {
    type = string
}
variable "container_port" {
    type = number
}
variable "subnets_id" {
    type = list(string)
}
variable "security_group_id" {
    type = string
}
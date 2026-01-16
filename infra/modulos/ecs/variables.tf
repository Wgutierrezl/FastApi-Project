variable "ecs_cluster_name" {
    type = string
}
variable "service_name_dev" {
    type = string
}
variable "service_name_prod" {
    type = string
}
variable "task_family_dev" {
    type = string
}
variable "task_family_prod" {
  type = string
}
variable "container_image_dev" {
    type = string
}
variable "container_image_prod" {
    type = string
}
variable "container_port_dev" {
    type = number
}
variable "container_port_prod" {
    type = number
}
variable "subnets_id" {
    type = list(string)
}
variable "security_group_id" {
    type = string
}
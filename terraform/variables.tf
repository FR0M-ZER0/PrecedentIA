variable "tenancy_ocid" { description = "OCID da Tenancy" }
variable "user_ocid" { description = "OCID do Usuário" }
variable "fingerprint" { description = "Fingerprint da chave da API" }
variable "private_key_path" { description = "Caminho para a chave privada (.pem)" }
variable "region" { default = "sa-saopaulo-1" }
variable "compartment_ocid" { description = "OCID do Compartimento (Tenancy)" }
variable "ssh_public_key" { description = "Chave publica SSH para acessar a VM" }
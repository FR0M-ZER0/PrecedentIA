output "ip_publico_da_maquina" {
  value = oci_core_instance.precedentia_vm.public_ip
}
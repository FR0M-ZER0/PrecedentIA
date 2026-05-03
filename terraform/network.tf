resource "oci_core_vcn" "precedentia_vcn" {
  compartment_id = var.compartment_ocid
  cidr_blocks    = ["10.0.0.0/16"]
  display_name   = "vcn-precedentia"
  dns_label      = "precedentia"
}

resource "oci_core_subnet" "precedentia_subnet_publica" {
  compartment_id = var.compartment_ocid
  vcn_id         = oci_core_vcn.precedentia_vcn.id
  cidr_block     = "10.0.1.0/24"
  display_name   = "subnet-publica-precedentia"
  dns_label      = "publica"
  route_table_id = oci_core_route_table.precedentia_route_table.id
}

resource "oci_core_internet_gateway" "precedentia_igw" {
  compartment_id = var.compartment_ocid
  vcn_id         = oci_core_vcn.precedentia_vcn.id
  enabled        = true
  display_name   = "igw-precedentia"
}

resource "oci_core_route_table" "precedentia_route_table" {
  compartment_id = var.compartment_ocid
  vcn_id         = oci_core_vcn.precedentia_vcn.id
  display_name   = "rt-publica-precedentia"

  route_rules {
    destination       = "0.0.0.0/0"
    destination_type  = "CIDR_BLOCK"
    network_entity_id = oci_core_internet_gateway.precedentia_igw.id
  }
}
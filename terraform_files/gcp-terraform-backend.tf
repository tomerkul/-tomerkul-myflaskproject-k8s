terraform {
  backend "gcs" {
    bucket      = "tomerkul-gke-terraform"
    prefix      = "terraform/state"
    credentials = "./macro-aurora-393206-e1e6e639aabe.json"
  }
}

module "gke" {
  source                     = "terraform-google-modules/kubernetes-engine/google"
  project_id                 = var.project_id
  name                       = var.name
  region                     = var.region
  zones                      = var.zones
  network                    = "default"
  subnetwork                 = "default"
  ip_range_pods              = ""
  ip_range_services          = ""
  http_load_balancing        = false
  network_policy             = true
  horizontal_pod_autoscaling = true
  filestore_csi_driver       = false

  node_pools = [
    {
      name             = "basic-node-pool"
      machine_type     = "n1-standard-1"  # Replace with desired machine type
      disk_size_gb     = 50             # Replace with desired disk size
      disk_type        = "pd-standard"   # Replace with desired disk type ("pd-standard" or "pd-ssd")
      image_type       = "COS_CONTAINERD"  # Specify the image type ("COS" or "COS_CONTAINERD")
      min_count        = 1               # Replace with minimum number of nodes
      max_count        = 1              # Replace with maximum number of nodes
      auto_repair      = true            # Enable auto repair
      auto_upgrade     = true            # Enable auto upgrade
      preemptible      = false           # Set to "true" if you want to use preemptible VMs
      initial_node_count = 1             # Replace with initial number of nodes
    }
  ]
}

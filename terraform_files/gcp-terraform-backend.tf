terraform {
  backend "gcs" {
    bucket      = "tomerkul-gke-terraform"
    prefix      = "terraform/state"
    credentials = "/var/lib/jenkins/terra/macro-aurora-393206-e1e6e639aabe.json"
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
      machine_type     = "n1-standard-1"  
      disk_size_gb     = 50            
      disk_type        = "pd-standard"  
      image_type       = "COS_CONTAINERD"  
      min_count        = 1               
      max_count        = 1            
      auto_repair      = true           
      auto_upgrade     = true          
      preemptible      = false         
      initial_node_count = 1    
    }
  ]
}

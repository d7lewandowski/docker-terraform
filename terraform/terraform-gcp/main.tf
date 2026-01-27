terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "7.16.0"
    }
  }
}

provider "google" {
  credentials = "/workspaces/docker-terraform/terraform/terraform-gcp/keys/dtc-de-course-485115-905d70784e1f.json"
  project = "dtc-de-course-485115"
  region  = "us-central1"
}


resource "google_storage_bucket" "demo-bucket" {
  name          = "dtc-de-course-485115-terra-bucket"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 3
    }
    action {
      type = "Delete"
    }
  }

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}
                                                                                 
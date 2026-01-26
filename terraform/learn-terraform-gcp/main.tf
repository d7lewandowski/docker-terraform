terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.8.0"
    }
  }
}

provider "google" {
  project = val.project
  region  = val.region
  zone    = val.zone
}

resource "google_compute_network" "vpc_network" {
  name = "terraform-network"
}


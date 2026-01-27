variable "credentials" {
  description = "My Credentials"
  default     = "/workspaces/docker-terraform/terraform/terraform-gcp/keys/abc_.json"
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}

variable "project" {
  description = "Project"
  default     = "dtc-de-course-485115"
}


variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}

variable "gcs_bucket_name" {
  default     = "dtc-de-course-485115-terra-bucket"
  description = "My storage bucket name"
}
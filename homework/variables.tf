variable "credentials" {
  description = "Google Cloud credentials"
  default     = "/workspaces/docker-terraform/terraform/dev/key_.json"
}


variable "project" {
  description = "Google Cloud project ID"
  default     = "dtc-de-course-485115"
}

variable "region" {
  description = "Google Cloud region"
  default     = "us-central1"
}

variable "bucket_name" {
  description = "Google Cloud bucket name"
  default     = "data-lake-bucket-dl7"
}

variable "location" {
  description = "Google Cloud location"
  default     = "US"
}

variable "dataset_id" {
  description = "BigQuery dataset ID"
  default     = "dataset_dl7"
}
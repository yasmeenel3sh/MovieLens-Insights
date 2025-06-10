terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.32.0"
    }
  }
}

provider "google" {
  project = var.project
  region  = var.region
} 

resource "google_storage_bucket" "demo-bucket" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }


  lifecycle_rule {
    condition {
      age=20
    }
    action {
      type = "Delete"
    }
  }
}

resource "google_bigquery_dataset" "Movielens_dataset" {
  dataset_id = var.bq_dataset_name
  location = var.location
  delete_contents_on_destroy = true 
}

resource "google_bigquery_dataset" "dev_dbt_dataset" {
  dataset_id = var.dbt_dev_dataset_name
  location = var.location
  delete_contents_on_destroy = true 
}
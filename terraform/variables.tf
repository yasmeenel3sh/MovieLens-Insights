

variable "project" {
    description = "Project"
    default = "terraform-basics-458014"
  
}

variable "region" {
    description = "region"
    default = "us-central1"
}

variable "location" {
    description = "Project Location"
    default = "US"
}

variable "bq_dataset_name" {
    description = "BigQuery dataset name"
    default = "movie_lens"
  
}

variable "gcs_storage_class" {
    description = "Bucket Storage Class"
    default = "STANDARD"  
}

variable "gcs_bucket_name" {
    description = "Storage Bucket Name"
    default = "terraform-basics-458014-movielens"
  
}
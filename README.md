# MovieLens-Insights: Data Engineering Project


This project showcases robust data engineering skills by building a comprehensive ELT (Extract, Load, Transform) pipeline for the MovieLens 1M dataset. The pipeline orchestrates various Google Cloud Platform (GCP) services and open-source tools to efficiently process, transform, and visualize data, demonstrating a full end-to-end data solution.


## Project Architecture

The following diagram illustrates the architecture of the ELT pipeline, highlighting the flow of data and the tools used at each stage:


---

## Pipeline Stages

### 1. Data Ingestion & Storage

* **MovieLens 1M dataset** files are initially uploaded to **Google Cloud Storage (GCS)**, acting as the raw data landing zone.

### 2. Data Loading & Schema Definition

* **External tables** are created in **BigQuery**, directly referencing the raw data stored in GCS. This allows for querying the data without physically moving it into BigQuery's managed storage.

### 3. Data Transformation

* **dbt (data build tool)** is employed to apply a series of **transformations** to the data within BigQuery. This stage cleans, structures, and aggregates the raw data into a format suitable for analysis.

### 4. Workflow Orchestration

* The entire ELT pipeline is **automated** using **Apache Airflow**, with the help of **Astronomer** for its managed services.
* **Cosmos** is integrated to further enhance the orchestration, especially for dbt projects within Airflow, ensuring a streamlined and efficient workflow execution.

### 5. Data Visualization

* A dynamic **dashboard** is built using **Looker Studio** to visualize the transformed data. This provides insightful analytics and allows for easy exploration of the MovieLens dataset.

### 6. Infrastructure as Code (IaC)

* **Terraform** is utilized to **provision the necessary infrastructure** on Google Cloud Platform. This approach ensures that the environment is consistent, reproducible, and scalable, adhering to modern DevOps practices.

## Pipeline graph

![MovieLens_Pipeline_graph](https://github.com/yasmeenel3sh/MovieLens-Insights/blob/main/Images/MovieLens_1M_pipeline-graph.png)

## [The Dashboard]

![Dashboard](https://github.com/yasmeenel3sh/MovieLens-Insights/blob/main/Images/Movielens_Insights.png)
# YouTube Data Engineering Project

## Objective

This project focuses on the efficient management, transformation, and analysis of YouTube video data. The goal is to understand viewing patterns across different categories and regions, helping to optimize targeted advertising strategies.

## Key Objectives
1. **Data Ingestion**: Develop a robust system to seamlessly ingest data from diverse sources.
2. **ETL Processes**: Transform raw data into a structured, analyzable format.
3. **Data Lake Management**: Centralize data storage to accommodate input from multiple sources.
4. **Scalability**: Ensure the architecture scales effectively with the growth of data volume.
5. **Cloud Integration**: Utilize AWS cloud infrastructure to handle large-scale data processing.
6. **Reporting**: Create an interactive dashboard for insightful data visualization and analysis.

## AWS Services Utilized
1. **Amazon S3**: A secure, scalable object storage service for centralized data storage.
2. **AWS IAM**: Identity and Access Management to securely control access to AWS resources.
3. **Amazon QuickSight**: A cloud-based BI service for creating interactive data dashboards.
4. **AWS Glue**: A serverless data integration service to automate ETL operations.
5. **AWS Lambda**: A serverless compute service for running code in response to events.
6. **AWS Athena**: A serverless query service that allows direct querying of data stored in S3.

## Dataset Description

The project uses a dataset from Kaggle, which contains daily statistics of trending YouTube videos across various regions. Each file represents a region and includes data like video title, channel title, publication time, views, likes, dislikes, tags, and comment count. A `category_id` field, specific to each region, is also included to categorize the videos.

[Link to the dataset](https://www.kaggle.com/datasets/datasnaek/youtube-new)

## Architecture Diagram
<img src="architecture.jpeg">

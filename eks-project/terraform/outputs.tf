output "ecr_repository_url" {
    value = aws_ecr_repository.my_repo.repository_url
}

output "sbom_bucket_url" {
  description = "URL do bucket S3"
  value       = "s3://${aws_s3_bucket.sbom_bucket.bucket}"
}

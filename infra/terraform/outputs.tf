output "ecr_gateway_repository_url" {
    value = aws_ecr_repository.gateway.repository_url
}

output "ecr_llm_repository_url" {
    value = aws_ecr_repository.llm.repository_url
}

output "ecr_storage_repository_url" {
    value = aws_ecr_repository.storage.repository_url
}

output "sbom_bucket_url" {
  description = "URL do bucket S3"
  value       = "s3://${aws_s3_bucket.sbom_bucket.bucket}"
}

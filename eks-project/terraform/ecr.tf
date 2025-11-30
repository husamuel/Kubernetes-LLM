resource "aws_ecr_repository" "my_repo" {
	name                 = "my_repo"

	image_tag_mutability = "MUTABLE"
	image_scanning_configuration {
		scan_on_push = true
	}

	tags = {
		Environment = "dev"
		Project     = "eks-learning"
	}
}

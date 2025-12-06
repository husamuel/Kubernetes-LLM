resource "aws_ecr_repository" "gateway" {
	name                 = "gateway"

	image_tag_mutability = "MUTABLE"
	image_scanning_configuration {
		scan_on_push = true
	}
}

resource "aws_ecr_repository" "llm" {
	name                 = "llm"

	image_tag_mutability = "MUTABLE"
	image_scanning_configuration {
		scan_on_push = true
	}
}
resource "aws_ecr_repository" "storage" {
	name                 = "storage"

	image_tag_mutability = "MUTABLE"
	image_scanning_configuration {
		scan_on_push = true
	}
}
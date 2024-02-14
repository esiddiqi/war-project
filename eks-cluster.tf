resource "aws_eks_cluster" "ems_eks_cluster" {
  name     = "ems-eks-cluster"
  role_arn = "arn:aws:iam::590184034959:role/eks-roll-emaad"
  vpc_config {
    subnet_ids = ["subnet-000e8acb912a54e4d", "subnet-05d51671a70fb1b9d"]
  }
}


resource "aws_eks_node_group" "ems_eks_node_group" {
  cluster_name  = "ems-eks-cluster"
  node_role_arn = "arn:aws:iam::590184034959:role/nodegroup_role"
  subnet_ids    = ["subnet-000e8acb912a54e4d", "subnet-05d51671a70fb1b9d"]
  scaling_config {
    desired_size = 1
    max_size     = 1
    min_size     = 1
  }

  depends_on = [aws_eks_cluster.ems_eks_cluster]
}





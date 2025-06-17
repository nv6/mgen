target "default" {
  dockerfile = rpm.Dockerfile
  output = [{
    type = "local"
    dest = "rpmbuild"
  }]
}
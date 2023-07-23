
import docker

client = docker.from_env()
images = client.images.list()

existing_versions = []
for image in images:
    if image.tags and image.tags[0].startswith("tomerkul/mysql:") and image.tags[0] != "tomerkul/mysql:latest":
        version_str = image.tags[0].split(":")[1]
        existing_versions.append(float(version_str))

if existing_versions:
    latest_version = max(existing_versions)
    next_version = latest_version + 0.01
else:
    next_version = 1.0

image_name = f"tomerkul/mysql:{next_version}"
client.images.build(path=".", tag=image_name, rm=True, pull=True)
print(f"Successfully built image: {image_name}")

# Push the image with the specified tag
client.images.push(repository="tomerkul/mysql", tag=str(next_version))
print(f"Successfully pushed image: {image_name}")

# Push the image with the 'latest' tag
latest_tag = "latest"
latest_image_name = f"tomerkul/mysql:{latest_tag}"
image_to_tag = client.images.get(image_name)
image_to_tag.tag(repository="tomerkul/mysql", tag=latest_tag)
client.images.push(repository="tomerkul/mysql", tag=latest_tag)
print(f"Successfully pushed image: {latest_image_name}")


import docker

client = docker.from_env()
images = client.images.list()

existing_versions = []
for image in images:
    if image.tags and image.tags[0].startswith("tomerkul/myflask:") and image.tags[0] != "tomerkul/myflask:latest":
        version_str = image.tags[0].split(":")[1]
        existing_versions.append(float(version_str))

if existing_versions:
    latest_version = max(existing_versions)
    next_version = round(latest_version + 0.01, 2)
else:
    next_version = 1.0

image_name = f"tomerkul/myflask:{next_version}"
client.images.build(path=".", tag=image_name, rm=True, pull=True)
print(f"Successfully built image: {image_name}")


client.images.push(repository="tomerkul/myflask", tag=str(next_version))
print(f"Successfully pushed image: {image_name}")


latest_tag = "latest"
latest_image_name = f"tomerkul/myflask:{latest_tag}"
image_to_tag = client.images.get(image_name)
image_to_tag.tag(repository="tomerkul/myflask", tag=latest_tag)
client.images.push(repository="tomerkul/myflask", tag=latest_tag)
print(f"Successfully pushed image: {latest_image_name}")

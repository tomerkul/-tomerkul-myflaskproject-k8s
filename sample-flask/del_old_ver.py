import docker

def find_max_version(images, repo_name, client):
    max_version = None
    for image in images:
        if image.tags:
            for tag in image.tags:
                if f"{repo_name}:latest" == tag:
                    print(f"Deleting image: {tag}")
                    try:
                        client.images.remove(tag, force=True)
                    except docker.errors.ImageNotFound:
                        print(f"Image {tag} not found. Skipping deletion.")
                    except docker.errors.APIError as e:
                        print(f"Error while deleting {tag}: {e}")
                elif f"{repo_name}:" in tag:
                    version = tag.replace(f"{repo_name}:", "")
                    if not max_version or version > max_version:
                        max_version = version
    return max_version

def delete_old_versions(images, repo_name, max_version, client):
    for image in images:
        if image.tags:
            for tag in image.tags:
                if f"{repo_name}:" in tag:
                    version = tag.replace(f"{repo_name}:", "")
                    if version != max_version:
                        print(f"Deleting image: {tag}")
                        try:
                            client.images.remove(tag, force=True)
                        except docker.errors.ImageNotFound:
                            print(f"Image {tag} not found. Skipping deletion.")
                        except docker.errors.APIError as e:
                            print(f"Error while deleting {tag}: {e}")

def main():
    repos = ["tomerkul/myflask", "tomerkul/mysql"]
    client = docker.from_env()
    all_images = client.images.list(all=True)

    for repo_name in repos:
        # Delete the image with the "latest" tag first
        max_version = find_max_version(all_images, repo_name, client)

        # Find the image with the highest numerical version of the specified repository
        max_version = find_max_version(all_images, repo_name, client)

        if max_version:
            print(f"Image with the maximum version of {repo_name}: {max_version}")

            # Delete all other versions of the specified repository, except the one with the max version
            delete_old_versions(all_images, repo_name, max_version, client)
        else:
            print(f"No {repo_name} images found.")

if __name__ == "__main__":
    main()

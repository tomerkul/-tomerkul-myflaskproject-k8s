import sys
import requests
from packaging.version import Version

def compare_versions(v1, v2):
    return Version(v1) > Version(v2)

def get_highest_version(repository):
    url = f"https://hub.docker.com/v2/repositories/tomerkul/{repository}/tags/?page_size=100"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        tags = data["results"]
        if not tags:
            return None

        max_version = None
        for tag in tags:
            tag_name = tag["name"]
            if tag_name == "latest":
                continue
            if max_version is None or compare_versions(tag_name, max_version):
                max_version = tag_name

        return max_version

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python get_highest_version.py <repository_name>")
        sys.exit(1)
    
    repository_name = sys.argv[1]
    highest_version = get_highest_version(repository_name)
    if highest_version:
        print(f"The highest version for {repository_name} is: {highest_version}")
    else:
        print(f"No versions found for {repository_name}")

import requests
import re
import yaml

def compare_versions(version1, version2):
    def normalize(v):
        return [int(x) for x in re.sub(r'(\.0+)*$', '', v).split(".")]

    return (normalize(version1) > normalize(version2)) - (normalize(version1) < normalize(version2))

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
            if max_version is None or compare_versions(tag_name, max_version) > 0:
                max_version = tag_name

        return max_version
    else:
        print(f"Error: Unable to fetch data for {repository}. Response status code: {response.status_code}")
        return None

def update_image_tags(yaml_data, high_flask, high_sql):
    for item in yaml_data:
        if "image" in item.get("spec", {}).get("template", {}).get("spec", {}).get("containers", [{}])[0]:
            image_tag = item["spec"]["template"]["spec"]["containers"][0]["image"]
            repository, _, tag = image_tag.rpartition(":")  # Use rpartition to handle tags with colons

            # Use the high_flask and high_sql variables directly instead of calling get_highest_version
            if repository == "tomerkul/myflask" and high_flask:
                item["spec"]["template"]["spec"]["containers"][0]["image"] = f"{repository}:{high_flask}"
            elif repository == "tomerkul/mysql" and high_sql:
                item["spec"]["template"]["spec"]["containers"][0]["image"] = f"{repository}:{high_sql}"

    return yaml_data


def main():
    with open("kubemyflask.yaml", "r") as file:
        yaml_data = list(yaml.safe_load_all(file))
    high_flask = get_highest_version("myflask")
    high_sql = get_highest_version("mysql")
    print("Highest Flask version:", high_flask)
    print("Highest MySQL version:", high_sql)

    updated_yaml_data = update_image_tags(yaml_data, high_flask, high_sql)

    with open("kubemyflask.yaml", "w") as file:
        yaml.safe_dump_all(updated_yaml_data, file)

if __name__ == "__main__":
    main()

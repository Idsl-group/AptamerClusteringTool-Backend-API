import yaml


def read_yaml(file_path: str) -> dict:
    """
    Reads a YAML file and returns the contents as a dictionary.

    :param file_path: Path to the YAML file.
    :return: Contents of the YAML file as a dictionary.
    """
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data


def write_yaml(file_path: str, data: dict) -> None:
    """
    Writes a dictionary to a YAML file.

    :param file_path: Path to the YAML file.
    :param data: Dictionary to write to the YAML file.
    """
    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file, default_flow_style=False)

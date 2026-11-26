import yaml

def load_config(file_path):
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            content = yaml.safe_load(file)

        if content is None:
            raise ValueError(f"YAML configuration file is empty: {file_path}")
        
        if not isinstance(content, dict):
            raise ValueError(f"Expected a YAML dictionary: {file_path}")
        
        return content
    
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML configuration: {file_path}") from e


output = load_config("config/processing_dates.yaml")
print(output["processing_rules"]["processing_dates"]["start_date"])
print(type(output["processing_rules"]["processing_dates"]["start_date"]))
# print(output)
# print(type(output))
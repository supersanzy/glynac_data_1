import re
from data_generator import config_loader

configs = config_loader.load_config("config/organisations.yaml")

def validate_organisation(config):
    """Validate the structure and values of the organisations configuration."""

    if ("organisations" in config and isinstance(config["organisations"], list) and config["organisations"]):
        # Loop through organisations
        for organisation in config["organisations"]:         
            # validates that each organisation is a dictionary                      
            if isinstance(organisation, dict):     
                # validates that org_id and name exists and if they do exist....                                 
                if "org_id" in organisation and "name" in organisation:         
                    # check if organisation values are strings and also not empty                    
                    if not isinstance(organisation["org_id"], str) or not organisation["org_id"].strip():                       
                        raise ValueError("org_id must be a non-empty string")
                    if not isinstance(organisation["name"], str) or not organisation["name"].strip():
                        raise ValueError("name must be a non-empty string")
                    if re.fullmatch(r"ORG_\d{3}", organisation["org_id"]) is None:      # validates that org_id value are not empty and is valid
                        raise ValueError("org_id must follow the format ORG_XXX")
                else:
                    raise ValueError("Each organisation must contain 'org_id' and 'name'")                            
            else:
                raise ValueError("Each organisation must be a dictionary")           
                   
        return True
    
    raise ValueError("Your YAML organisations configuration is invalid")
       
output = validate_organisation(config=configs)
print(output)


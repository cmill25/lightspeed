from src.api.client import get_data
import json

def main():
    data = get_data('products')
    
    product_names = []
    for i in data['data']:
        metadata = {
            'name': i['name'],
            'has_variants': i['has_variants'],
            'variant_name': i['variant_name']
        }
        product_names.append(metadata)
    
    print(json.dumps(product_names, indent=4))

main()

#prob just want to grab all the names and scids
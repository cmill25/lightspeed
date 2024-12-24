from src.api.client import get_data, search_data
import json

#def main():
#    data = get_data('suppliers')
#    
#    file_name = "suppliers.json"
#    with open(file_name, "w") as json_file:
#        json.dump(data, json_file, indent=4)

def main():
    entity = 'products'
    params = {
        'supplier_id': '943c2af1-887e-459b-b4ee-6df517e205c4'
    }
    product_names = []

    data = search_data(entity, params)
    for i in data['data']:
        metadata = {
            'name': i['name'],
            'has_variants': i['has_variants'],
            'variant_name': i['variant_name']
        }
        product_names.append(metadata)
    
    file_name = "response.json"
    with open(file_name, "w") as json_file:
        json.dump(product_names, json_file, indent=4)

main()

#prob just want to grab all the names and scids
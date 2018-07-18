from jsonschema import validate
from json import load

schema = load(open('Product-json.schema'))
data = load(open('products.json'))

validate(data, schema)
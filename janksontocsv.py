import json
from copy import deepcopy
from codecs import open as open
import uuid
import sys
import csv

print("\n\n----JSON to CSV (with key remover)----\n\n")
print("Wherever you run this, it will output 2 files. One csv and one json of the "
      "cleansed data.\n")

keys_to_remove = ['threads']
input_filename = ""
out_csv_file_name = ""
out_json_file_name = ""


# Remove the desired keys
def clean_obj(obj_json):
    rjson = deepcopy(obj_json)
    for key in keys_to_remove:
        if key in obj_json.keys():
            rjson[key] = ""
    return rjson


def print_help():
    print("Keys to remove: " + str(keys_to_remove))
    print("File: " + input_filename)
    print("Out CSV File: " + out_csv_file_name)
    print("Out JSON File: " + out_json_file_name)


# Get input with context of python version
if sys.version_info[0] < 3:
    input_filename = raw_input("What is the file name: ").rstrip()
else:
    input_filename = input("What is the file name: ").rstrip()

# Make out file names
u = str(uuid.uuid4())
out_csv_file_name = u + "_out.csv"
out_json_file_name = u + "_out.json"

print_help()
# Open the file
with open(input_filename, "r") as f1:
    j1 = json.load(f1)

output_json = []

# Clean the json of the desired keys
for obj in j1:
    output_json.append(clean_obj(obj))

# Write the json file
with open(out_json_file_name, "w") as outfile:
    print("Writing json file")
    outfile.write(json.dumps(output_json))

# Write the csv file
print("Writing csv file")

with open(out_csv_file_name, "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(output_json[0].keys())
    
    for obj in output_json:
        vals = []
        for key in output_json[0].keys():
            try:
                vals.append(str(obj[key]))
            except Exception:
                vals.append("")
        writer.writerow(vals)

print("Done")
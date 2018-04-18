# Jank-SON-to-CSV
Customizable JSON to CSV short cli


Run with `python janksontocsv.py`

Input the file name. (You can drag and drop it from finder)

Output will be put in format similar to 
84344b6c-fd10-46b2-82f9-9214f66b9c66_out.csv
84344b6c-fd10-46b2-82f9-9214f66b9c66_out.json

To customize what keys are removed, just add to the line that defines what keys are removed:
`keys_to_remove = ['threads']`

Ex: 
`keys_to_remove = ['threads', 'key2', 'key3']`


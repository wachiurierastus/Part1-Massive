import json

# Define the file paths for your language-specific JSON files
json_file_paths = ['en-US.jsonl', 'sw-KE.jsonl', 'de-DE.jsonl']

# Define the output directory where you want to save the split files
output_directory = 'Output'

# Create dictionaries to store data for each partition
data_partitions = {
    'train': [],
    'test': [],
    'dev': []
}

# Iterate through each language-specific JSON file
for file_path in json_file_paths:
    with open(file_path, 'r') as file:
        data = json.loads(file.read(), separators=('/', '\n'))
        data_partitions.append(data)

    # Iterate through the data and separate by partition
    for item in data:
        partition = item.get('partition', '').lower()
        if partition in data_partitions:
            data_partitions[partition].append(item)

# Save the split data to separate JSON files for each partition
for partition, partition_data in data_partitions.items():
    output_file = f'{output_directory}{partition}.json'
    with open(output_file, 'w', encoding='utf-8') as output_file:
        json.dump(partition_data, output_file, ensure_ascii=False, indent=4)

print("Data separation and saving complete.")

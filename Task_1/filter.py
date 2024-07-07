import pandas as pd

file_path = 'clustering_data.csv'  
data = pd.read_csv(file_path)


circle_name = 'Andhra Pradesh Circle'  


filtered_data = data[data['CircleName'] == circle_name]


output_file_path = 'filtered_data.csv'  
filtered_data.to_csv(output_file_path, index=False)

print(f"Filtered data saved to {output_file_path}")

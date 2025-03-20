import pandas as pd
import sys
import os
print("file load.py runs good")
def dataset_provider(csv_dataset_path):
    dataset = pd.read_csv(csv_dataset_path)
    print("Dataset loaded successfully!")

    # Save the dataset inside the container directory
    processed_path = "/home/doc-bd-a1/loaded_data.csv"
    dataset.to_csv(processed_path, index=False)

    print("Dataset saved in:", processed_path)
    return processed_path
  
if __name__ == "__main__":
    csv_path = sys.argv[1]
    processed_path = dataset_provider(csv_path)

    # Call dpre.py and pass the dataset path
    os.system(f"python3 dpre.py {processed_path}")
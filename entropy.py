import os
import pandas as pd
from file_object import FileClass  # Import your FileClass module
import hashlib

# Specify the folder path containing your files
folder_path = r"C:\Users\ayseg\OneDrive\Masaüstü\CYBER_DOSYA"

# Create an empty DataFrame to store the results
columns = ["file_path", "entropy", "hash_md5", "hash_sha1", "hash_sha256", "signature", "encrypted"]
result_df = pd.DataFrame(columns=columns)

# Iterate through files in the folder
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    # Check if the path is a file (not a directory)
    if os.path.isfile(file_path):
        # Use the FileClass to extract entropy, signature, and file string
        try:
            file_instance = FileClass(file_path)
            file_entropy = file_instance.calculate_entropy()
            file_signature = file_instance.get_signature()
            hash_md5 = file_instance.calc_file_hash_md5()
            hash_sha1 = file_instance.calc_file_hash_sha1()
            hash_sha256 = file_instance.calc_file_hash_sha256()
            encrypted=file_instance.is_encrypted()

            # Append results to DataFrame
            result_df = result_df.append({
                "file_path": file_path,
                "entropy": file_entropy,
                "hash_md5": hash_md5,
                "hash_sha1": hash_sha1,
                "hash_sha256": hash_sha256,
                "signature": file_signature,
                "encrypted":encrypted
            }, ignore_index=True)
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

# Save the DataFrame to a CSV file
result_df.to_csv("analysis_results.csv", index=False)

# Display the first few rows of the resulting DataFrame
print(result_df.head())

import os
import subprocess
import sys

def download_kaggle_dataset(link, kaggle_json_path, download_dir="kaggle_datasets"):
    # Ensure kaggle.json exists
    if not os.path.exists(kaggle_json_path):
        print(f"Error: Kaggle API key file not found at {kaggle_json_path}.")
        sys.exit(1)

    # Set up Kaggle configuration
    os.makedirs(os.path.expanduser("~/.kaggle"), exist_ok=True)
    kaggle_config_path = os.path.expanduser("~/.kaggle/kaggle.json")
    
    if not os.path.exists(kaggle_config_path):
        os.rename(kaggle_json_path, kaggle_config_path)
        os.chmod(kaggle_config_path, 0o600)

    # Extract the dataset identifier from the link
    if "kaggle.com" not in link:
        print("Error: Invalid Kaggle link.")
        sys.exit(1)

    try:
        dataset_identifier = link.split("datasets/")[1]
    except IndexError:
        print("Error: Could not extract dataset identifier from the link.")
        sys.exit(1)

    # Ensure download directory exists
    os.makedirs(download_dir, exist_ok=True)

    # Use Kaggle CLI to download the dataset
    print(f"Downloading dataset {dataset_identifier}...")
    result = subprocess.run(
        ["kaggle", "datasets", "download", "-d", dataset_identifier, "-p", download_dir, "--unzip"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    if result.returncode == 0:
        print(f"Dataset downloaded successfully to {download_dir}.")
    else:
        print(f"Error downloading dataset: {result.stderr}")

# Example usage
if __name__ == "__main__":
    kaggle_link = "https://www.kaggle.com/datasets/mdkabinhasan/sports-ball-dataset"
    
    if len(sys.argv) < 2:
        print("Usage: python trial.py <path_to_kaggle_json>")
        sys.exit(1)
    
    kaggle_json_path = sys.argv[1]
    download_kaggle_dataset(kaggle_link, kaggle_json_path=kaggle_json_path)

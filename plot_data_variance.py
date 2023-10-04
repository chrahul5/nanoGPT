import subprocess
import data.sherlock_holmes_char.prepare as prepare

# Specify the name of the Python file you want to run
prepare_file = "data/sherlock_holmes_char/prepare.py"
train_file = "train.py"

try:
    # Format the dataset using prepare file.

    prepare.format_all_stories()

    for i in range(6, 67, 10):
        # Run prepare using i num of files
        subprocess.run(["python3", prepare_file, f'--num_files={i}'], check=True)
        # Train model using the dataset prepared.
        subprocess.run(["python3", train_file, 'config/train_sherlock_holmes'], check=True)
except FileNotFoundError:
    print(f"File '{prepare_file}' not found.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")

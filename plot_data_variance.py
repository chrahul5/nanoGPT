import subprocess

# Dataset.
prepare_file = "data/sherlock_holmes_char/prepare.py"
train_file = "train.py"
sample_file = "sample.py"

try:
    # Format the dataset using prepare file.
    for i in range(6, 67, 10):
        # Run prepare using i num of files
        subprocess.run(["python3", prepare_file, f'--num_files={i}'], check=True)
        print('########################################################################')
        # Train model using the dataset prepared.
        subprocess.run(["python3", train_file, 'config/train_sherlock_holmes_char.py', f'--out_dir=out-sherlock-holmes-char-train-{i}', '--compile=False'], check=True)
        print('########################################################################')
         # Sample output from model.
        subprocess.run(["python3", sample_file, f'--out_dir=out-sherlock-holmes-char-train-{i}', f'>> out-sherlock-holmes-char-train-{i}.txt'], check=True)
        print('########################################################################')
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")

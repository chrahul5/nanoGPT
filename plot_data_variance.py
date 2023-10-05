import subprocess
import fileinput

# Dataset.
prepare_file = "data/sherlock_holmes_char/prepare.py"
train_file = "train.py"
sample_file = "sample.py"

try:
    # Format the dataset using prepare file.
    for i in range(6, 67, 10):
        # Run prepare using i num of files
        # subprocess.run(["python3", prepare_file, f'--num_files={i}'], check=True)
        print('########################################################################')
        # Train model using the dataset prepared.
        # max_iters = 1000 if i < 30 else 2000
        # subprocess.run(["python3", train_file, 'config/train_sherlock_holmes_char.py', f'--out_dir=out-sherlock-holmes-char-train-{i}', f'--max_iters={max_iters}'], check=True)
        print('########################################################################')
         # Sample output from model.
        # Open the output file in write mode
        file_path = f'out-sherlock-holmes-train-{i}.txt'
        with open(file_path, "w") as file:
            subprocess.run(["python3", sample_file, f'--out_dir=out-sherlock-holmes-char-train-{i}', '--num_samples=1', '--max_new_tokens=10000'], stdout=file, check=True)
        print(f'sample output written to {file_path}')

        with fileinput.input(file_path, inplace=True) as file:
            for line_number, line in enumerate(file, start=1):
                if line_number > 6:
                    print(line, end='')
        print('########################################################################')
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")

# python3 data/sherlock_holmes_char/prepare.py --num_files=1
# python3 train.py config/train_sherlock_holmes_char.py --max_iters=250 --out_dir=out-sherlock-holmes-char-train-1
# step 250: train loss 1.5971, val loss 1.8574
# python3 sample.py --out_dir=out-sherlock-holmes-char-train-1 --num_samples=1 --max_new_tokens=5000

# python3 data/sherlock_holmes_char/prepare.py --num_files=6
# python3 train.py config/train_sherlock_holmes_char.py --max_iters=1000 --out_dir=out-sherlock-holmes-char-train-6
# step 250: train loss 1.5971, val loss 1.8574
# python3 sample.py --out_dir=out-sherlock-holmes-char-train-1 --num_samples=1 --max_new_tokens=5000

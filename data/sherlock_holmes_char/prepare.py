"""
Prepare the Sherlock Holmes dataset for character-level language modeling.
So instead of encoding with GPT-2 BPE tokens, we just map characters to ints.
Will save train.bin, val.bin containing the ids, and meta.pkl containing the
encoder and decoder and some other related info.
"""
import os
import pickle
import requests
import numpy as np
import replacer
import sys
import argparse

# download the sherlock_holmes dataset and place it here.
# TODO: Use kaggle API to download dataset if not present.
story_path = os.path.join(os.path.dirname(__file__), 'sherlock_holmes_stories/')

def format_all_stories(story_path):
    for _, _, files in os.walk(story_path):
        files_to_read = files

        for file in files_to_read:
            stories_txt = ""
            with open(story_path+file, 'r') as f:
                stories_txt = str(f.read())

            stories_txt = str(replacer.replace_characters(stories_txt))

            with open(story_path+file, 'w') as f:
                f.write(stories_txt)

            # print(stories_txt)

    return stories_txt

def read_all_stories(story_path, num_to_read=-1):
    stories_txt = ""
    for _, _, files in os.walk(story_path):
        files_to_read = files
        if num_to_read >= 0:
            files_to_read = files[:num_to_read]

        for file in files_to_read:
            with open(story_path+file, 'r') as f:
                stories_txt += f.read()
                # stories_txt += "!!!THE END!!!"

    return stories_txt


############# MAIN CODE ########################

parser = argparse.ArgumentParser()

parser.add_argument('--num_files', type=int, default=-1, help='Number of stories to be used for dataset')
parser.add_argument('--format_dataset', type=bool, default=False, help='Whether to format sherlock holmes dataset')

# Parse the command line arguments
args = parser.parse_args()

# Access the values of the parsed arguments
num_stories = args.num_files
format_dataset = args.format_dataset

if format_dataset:
    format_all_stories(story_path)
    print("Formatting dataset completed.")

data = read_all_stories(story_path, num_stories)
# data = replacer.replace_characters(data)
print(f"length of dataset in characters: {len(data):,}")

# get all the unique characters that occur in this text
chars = sorted(list(set(data)))
vocab_size = len(chars)
print("Unique characters in the dataset:", ''.join(chars))
print(f"vocab size: {vocab_size:,}")

# create a mapping from characters to integers
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
def encode(s):
    return [stoi[c] for c in s] # encoder: take a string, output a list of integers
def decode(l):
    return ''.join([itos[i] for i in l]) # decoder: take a list of integers, output a string

# create the train and test splits
n = len(data)
train_data = data[:int(n*0.9)]
val_data = data[int(n*0.9):]

# encode both to integers
train_ids = encode(train_data)
val_ids = encode(val_data)
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")

# export to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))

# save the meta information as well, to help us encode/decode later
meta = {
    'vocab_size': vocab_size,
    'itos': itos,
    'stoi': stoi,
}
with open(os.path.join(os.path.dirname(__file__), 'meta.pkl'), 'wb') as f:
    pickle.dump(meta, f)

# length of dataset in characters: 13,821,242
# all the unique characters: 
#  !"&'()*,-./0123456789:;?ABCDEFGHIJKLMNOPQRSTUVWXYZ[]`abcdefghijklmnopqrstuvwxyz£°½ßàâèéêîñôöûü’
# vocab size: 97
# train has 12,439,117 tokens
# val has 1,382,125 tokens
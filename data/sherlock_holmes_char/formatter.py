import os
import replacer

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

format_all_stories(story_path)
print("Formatting dataset completed.")
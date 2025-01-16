
# Exercise: File Handler
# Learn how to use Github Copilot for file operations

# TODO: Write a function that reads a file and counts the occurrences of each word
def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

# TODO: Write a function that writes a dictionary to a JSON file
def write_to_json(data, filename):
    import json
    with open(filename, 'w') as file:
        json.dump(data, file)

# TODO: Write a function that merges two text files
def merge_files(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        for line in f1:
            out.write(line)
        for line in f2:
            out.write(line)
wordCount = {}
with open('sample_text_file.txt', 'r') as file:
    for line in file:
        line = line.strip()
        wordCount[line] = wordCount.get(line, 0) + 1
print(wordCount)
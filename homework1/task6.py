"""
Create two new files named task6.py and task6_read_me.txt.
Then write a program inside task6.py of that reads task6_read_me.txt 
and counts the number of words in it. Implement metaprogramming
techniques to dynamically generate function names for your pytest 
test cases based on the filenames of the text files. Include pytest 
test cases that verify the word count for each text file.
"""

def get_file_word_count(filename):
    with open(filename, "r") as file:
        text = file.read().strip()
        char_chunks = text.split()

        words = []
        for chunk in char_chunks: 
            if not chunk == "." and not chunk == ",":
                words.append(chunk)
        
        return len(words)


if __name__ == "__main__":
    print(get_file_word_count("/home/student/cs5300/homework1/task6_read_me.txt"))

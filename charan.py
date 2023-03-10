import argparse
import os
import fileinput
import unittest


def replace_word_in_file(file_path, old_word, new_word):
    with fileinput.FileInput(file_path, inplace=True) as file:
        for line in file:
            print(line.replace(old_word, new_word), end='')


class TestReplaceWordInFiles(unittest.TestCase):
    def setUp(self):
        with open('test.txt', 'w') as f:
            f.write('charan is riding a bike.\n')

    def test_replace_word_in_file(self):
        replace_word_in_file('test.txt', 'bike', 'car')

        # To Verify The old word with the new word
        with open('test.txt') as f:
            contents = f.read()
            self.assertIn('car', contents)

    def tearDown(self):
        os.remove('test.txt')


if __name__ == '_main_':
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Replace a given word with a specific word in a file or files')
    parser.add_argument('old_word', type=str, help='The word to be replaced')
    parser.add_argument('new_word', type=str, help='The word to replace the old word')
    parser.add_argument('files', nargs='+', help='The files to modify')
    args = parser.parse_args()

    replace_word_in_file(args.files, args.old_word, args.new_word)

    unittest.main(argv=['first-arg-is-ignored'], exit=False)

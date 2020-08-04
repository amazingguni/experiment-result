import csv
word_diffs = []
line_diffs = []

WORD_END = ['</add>', '</delete>']


LINE_ADD = '<add>'
LINE_DELETE = '<delete>'
LINE_SAME = '<same>'
MODE_ADD = 1
MODE_DELETE = 2
MODE_SAME = 3

def calculate_diff_word(s):
    add_word = []
    delete_word = []
    mode = 3
    for word in s.split():
        if word == LINE_ADD:
            mode = MODE_ADD
            continue
        if word == LINE_DELETE:
            mode = MODE_DELETE
            continue
        if word in WORD_END:
            mode = MODE_SAME
            continue
        if mode == MODE_ADD:
            add_word.append(word)
            continue
        if mode == MODE_DELETE:
            delete_word.append(word)
            continue
    return len(add_word) + len(delete_word), len(add_word), len(delete_word)

def calculate_diff_line(s):
    diff_cnt = 0
    add_word = []
    delete_word = []
    mode = 3
    for word in s.split():
        if word == LINE_ADD:
            mode = MODE_ADD
            continue
        if word == LINE_DELETE:
            mode = MODE_DELETE
            continue
        if word == LINE_SAME:
            mode = MODE_SAME
            continue
        if mode == MODE_ADD:
            add_word.append(word)
            continue
        if mode == MODE_DELETE:
            delete_word.append(word)
            continue
    return len(add_word) + len(delete_word), len(add_word), len(delete_word)

def compare_diff_cnt(word, line):
    line, line_add_word, line_delete_word = calculate_diff_line(line)
    word, word_add_word, word_delete_word = calculate_diff_word(word)
    return line, word


dataset = 'java2000'

with open(f'{dataset}-word-compare-2.csv', newline='') as f_word,\
    open(f'{dataset}-line-compare-2.csv', newline='') as f_line,\
    open(f'{dataset}-merged-compare-2.csv', 'w') as f_merge:
    reader_word = csv.reader(f_word)
    reader_line = csv.reader(f_line)
    writer = csv.writer(f_merge, delimiter=',')
    correct, incorrect = 0, 0
    for word_row, line_row in zip(reader_word, reader_line):
        line_src = line_row[2]
        word_src = word_row[2]
        word, line = compare_diff_cnt(word_src, line_src)
        diff_cnt = line - word
        if diff_cnt == 0:
            correct += 1
        else:
            incorrect += 1
        writer.writerow(word_row + line_row + [word, line, diff_cnt, diff_cnt == 0])
    print(correct, incorrect)

   

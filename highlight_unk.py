
import argparse
from pathlib import Path


def get_highlight_str(vocab_dic, s):
    oov_words = []
    words = []
    for w in s.split():
        if w in vocab_dic:
            words.append(w)
        else:
            words.append(f'__{w}__')
            oov_words.append(w)
    return ' '.join(words), oov_words


def highlight_unk(vocab_file, pred_file, ref_file):
    vocab_dic = {}
    with open(vocab_file) as f:
        vocab_dic = {word: True for word in str(f.read()).strip().split('\n')}

    f_ref_highlight = open(str(ref_file) + '.highlight', 'w')
    f_pred_highlight = open(str(pred_file) + '.highlight', 'w')

    f_ref = open(ref_file)
    f_pred = open(pred_file)

    total_ref_oov_cnt = 0
    correct_pred_copy_cnt = 0
    total_pred_oov_cnt = 0
    total_word_cnt = 0
    for ref, pred in zip(f_ref, f_pred):
        total_word_cnt += len(ref.split())
        highlight_ref, ref_oovs = get_highlight_str(vocab_dic, ref.strip())
        highlight_pred, pred_oovs = get_highlight_str(vocab_dic, pred.strip())
        f_ref_highlight.write(highlight_ref + '\n')
        f_pred_highlight.write(highlight_pred + '\n')
        total_ref_oov_cnt += len(ref_oovs)
        total_pred_oov_cnt += len(pred_oovs)
        correct_oovs_cnt = 0
        for w in pred_oovs:
            if w in ref_oovs:
                correct_oovs_cnt += 1
                ref_oovs.remove(w)
        correct_oovs = list(set(ref_oovs) & set(pred_oovs))
        if correct_oovs_cnt != len(correct_oovs):
            pass
            #print(correct_oovs_cnt, len(correct_oovs))
        #correct_pred_copy_cnt += len(correct_oovs)
        correct_pred_copy_cnt += correct_oovs_cnt
    print(pred_file)
    recall = correct_pred_copy_cnt / total_ref_oov_cnt
    precision = correct_pred_copy_cnt / total_pred_oov_cnt
    print(f' * correct_pred_copy_cnt: {correct_pred_copy_cnt}')
    print(f' * total_ref_oov_cnt: {total_ref_oov_cnt}')
    print(f' * total_pred_oov_cnt: {total_pred_oov_cnt}')
    print(f' * total_word_cnt: {total_word_cnt}')
    f_1 = (2 * precision * recall) / (precision + recall)
    print(f' * recall: {recall}')
    print(f' * precision: {precision}')
    print(f' * f_1: {f_1}')

def handle_dataset(dataset):
    vocab_file = dataset / 'vocab'
    ref = dataset / 'copytransformer.ref'
    pred = dataset / 'copytransformer.pred'
    if pred.exists():
        highlight_unk(vocab_file, pred, ref)
    pred = dataset / 'pgnet.pred'
    if pred.exists():
        highlight_unk(vocab_file, pred, ref)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--path', type=str, required=True)
    args = parser.parse_args()
    root_path = Path(args.path)
    line = root_path / 'line'
    word = root_path / 'word'
    handle_dataset(word)
    handle_dataset(line)
#    highlight_unk(line)
#    highlight_unk(line)

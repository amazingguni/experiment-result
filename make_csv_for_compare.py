import csv
from rouge_score import rouge_scorer
from nltk.translate.bleu_score import sentence_bleu
from math import isclose

from pathlib import Path

def make_csv(dataset, dataset_type):
 #   DATASET= 'java2000' # 'python1000' #'java2000' 
 #   TYPE= 'line' # 'word' # 'line'

    target = Path('.') / dataset / dataset_type
    csv_filename = f'{dataset}-{dataset_type}-compare-2.csv'

    with open(target / 'index') as f:
        indexes = f.read().strip().split('\n')
    with open(target / 'copytransformer.ref') as f:
        references = f.read().strip().split('\n')
    with open(target / 'transformer.pred') as f:
        transformer_predicts = f.read().strip().split('\n')
    with open(target / 'copytransformer.pred') as f:
        copytransformer_predicts = f.read().strip().split('\n')
    with open(target / 'pgnet.pred') as f:
        pgnet_predicts = f.read().strip().split('\n')
    with open(target / 'source') as f:
        sources = f.read().strip().split('\n')

    scorer = rouge_scorer.RougeScorer(
        ['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    pairs = []


    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for index, ref, copy_pred, trans_pred, pgnet_pred, source in zip(indexes, references, copytransformer_predicts, transformer_predicts, pgnet_predicts, sources):
        #for index, ref, copy_pred, pgnet_pred in zip(indexes, references, copytransformer_predicts, pgnet_predicts):
            ref_words = ref.split()
            copy_bleu = sentence_bleu([ref_words], copy_pred.split())
            trans_bleu = sentence_bleu([ref_words], trans_pred.split())
            pgnet_bleu = sentence_bleu([ref_words], pgnet_pred.split())
            copy_rouge = scorer.score(ref, copy_pred)['rougeL'].recall
            trans_rouge = scorer.score(ref, trans_pred)['rougeL'].recall
            pgnet_rouge = scorer.score(ref, pgnet_pred)['rougeL'].recall

            fullpath, sha = index.strip().split()
            url = f'https://github.com/{fullpath}/commit/{sha}'
            row = [url, ref, source]
            row += [copy_pred, copy_bleu, copy_rouge]
            row += [trans_pred, trans_bleu, trans_rouge]
            row += [pgnet_pred, pgnet_bleu, pgnet_rouge]
            writer.writerow(row)


make_csv('java1000', 'word')
make_csv('java1000', 'line')
make_csv('java2000', 'word')
make_csv('java2000', 'line')
make_csv('python1000', 'word')
make_csv('python1000', 'line')

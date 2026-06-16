import torch
from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.meteor_score import meteor_score
from rouge import Rouge

def calculate_bleu(reference, hypothesis):
    """
    Calculate BLEU score between reference and hypothesis sentences.
    """
    # For Vietnamese sentences, we need to tokenize them first
    # This is a simplified implementation
    reference = [ref.split() for ref in reference]
    hypothesis = [hyp.split() for hyp in hypothesis]
    
    bleu_scores = []
    for ref, hyp in zip(reference, hypothesis):
        score = sentence_bleu([ref], hyp)
        bleu_scores.append(score)
    
    return sum(bleu_scores) / len(bleu_scores)

def calculate_meteor(reference, hypothesis):
    """
    Calculate METEOR score between reference and hypothesis sentences.
    """
    # For Vietnamese sentences
    meteor_scores = []
    for ref, hyp in zip(reference, hypothesis):
        try:
            score = meteor_score([ref.split()], hyp.split())
            meteor_scores.append(score)
        except:
            # If METEOR can't be calculated, return 0
            meteor_scores.append(0)
    
    return sum(meteor_scores) / len(meteor_scores)

def calculate_rouge(reference, hypothesis):
    """
    Calculate ROUGE score between reference and hypothesis sentences.
    """
    rouge = Rouge()
    scores = []
    for ref, hyp in zip(reference, hypothesis):
        try:
            score = rouge.get_scores(hyp, ref)
            scores.append(score[0]['rouge-1']['f'])
        except:
            scores.append(0)
    
    return sum(scores) / len(scores)
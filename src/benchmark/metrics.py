import time
import torch

class MetricsTracker:
    def __init__(self):
        self.training_times = []
        self.inference_times = []
        self.memory_usage = []
        self.bleu_scores = []
        self.rouge_scores = []
        self.meteor_scores = []
        
    def start_timer(self):
        """Start timing a process."""
        self.start_time = time.time()
        
    def end_timer(self):
        """End timing and record the duration."""
        end_time = time.time()
        return end_time - self.start_time
        
    def record_training_time(self, duration):
        """Record training time."""
        self.training_times.append(duration)
        
    def record_inference_time(self, duration):
        """Record inference time."""
        self.inference_times.append(duration)
        
    def record_memory_usage(self, memory):
        """Record memory usage."""
        self.memory_usage.append(memory)
        
    def record_bleu(self, score):
        """Record BLEU score."""
        self.bleu_scores.append(score)
        
    def record_rouge(self, score):
        """Record ROUGE score."""
        self.rouge_scores.append(score)
        
    def record_meteor(self, score):
        """Record METEOR score."""
        self.meteor_scores.append(score)
        
    def get_average_training_time(self):
        """Get average training time."""
        return sum(self.training_times) / len(self.training_times) if self.training_times else 0
        
    def get_average_inference_time(self):
        """Get average inference time."""
        return sum(self.inference_times) / len(self.inference_times) if self.inference_times else 0
        
    def get_average_memory_usage(self):
        """Get average memory usage."""
        return sum(self.memory_usage) / len(self.memory_usage) if self.memory_usage else 0
        
    def get_average_bleu(self):
        """Get average BLEU score."""
        return sum(self.bleu_scores) / len(self.bleu_scores) if self.bleu_scores else 0
        
    def get_average_rouge(self):
        """Get average ROUGE score."""
        return sum(self.rouge_scores) / len(self.rouge_scores) if self.rouge_scores else 0
        
    def get_average_meteor(self):
        """Get average METEOR score."""
        return sum(self.meteor_scores) / len(self.meteor_scores) if self.meteor_scores else 0
import matplotlib.pyplot as plt
import numpy as np

class BenchmarkVisualizer:
    def __init__(self, metrics_tracker):
        self.metrics = metrics_tracker
        
    def plot_training_times(self):
        """Plot training times for both models."""
        plt.figure(figsize=(10, 6))
        models = ['LSTM', 'Transformer']
        times = [self.metrics.get_average_training_time()] * 2  # Placeholder data
        
        plt.bar(models, times)
        plt.title('Average Training Time Comparison')
        plt.ylabel('Time (seconds)')
        plt.show()
        
    def plot_inference_times(self):
        """Plot inference times for both models."""
        plt.figure(figsize=(10, 6))
        models = ['LSTM', 'Transformer']
        times = [self.metrics.get_average_inference_time()] * 2  # Placeholder data
        
        plt.bar(models, times)
        plt.title('Average Inference Time Comparison')
        plt.ylabel('Time (seconds)')
        plt.show()
        
    def plot_bleu_scores(self):
        """Plot BLEU scores for both models."""
        plt.figure(figsize=(10, 6))
        models = ['LSTM', 'Transformer']
        scores = [self.metrics.get_average_bleu()] * 2  # Placeholder data
        
        plt.bar(models, scores)
        plt.title('Average BLEU Score Comparison')
        plt.ylabel('BLEU Score')
        plt.show()
        
    def plot_all_metrics(self):
        """Plot all metrics in a comprehensive dashboard."""
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # Training times
        models = ['LSTM', 'Transformer']
        train_times = [self.metrics.get_average_training_time()] * 2
        axes[0, 0].bar(models, train_times)
        axes[0, 0].set_title('Training Time')
        axes[0, 0].set_ylabel('Time (seconds)')
        
        # Inference times
        infer_times = [self.metrics.get_average_inference_time()] * 2
        axes[0, 1].bar(models, infer_times)
        axes[0, 1].set_title('Inference Time')
        axes[0, 1].set_ylabel('Time (seconds)')
        
        # BLEU scores
        bleu_scores = [self.metrics.get_average_bleu()] * 2
        axes[1, 0].bar(models, bleu_scores)
        axes[1, 0].set_title('BLEU Scores')
        axes[1, 0].set_ylabel('Score')
        
        # ROUGE scores
        rouge_scores = [self.metrics.get_average_rouge()] * 2
        axes[1, 1].bar(models, rouge_scores)
        axes[1, 1].set_title('ROUGE Scores')
        axes[1, 1].set_ylabel('Score')
        
        plt.tight_layout()
        plt.show()
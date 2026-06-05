import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import random
import math
import time

# Evaluation functions would go here
def evaluate(model, iterator, criterion):
    model.eval()
    epoch_loss = 0
    
    with torch.no_grad():
        for i, batch in enumerate(iterator):
            src = batch.src
            trg = batch.trg
            
            output = model(src, trg, 0) # Turn off teacher forcing
            # output = [trg len, batch size, output dim]
            # trg = [trg len, batch size]
            
            output_dim = output.shape[-1]
            
            output = output[1:].view(-1, output_dim)
            trg = trg[1:].view(-1)
            # output = [trg len * batch size, output dim]
            # trg = [trg len * batch size]
            
            loss = criterion(output, trg)
            epoch_loss += loss.item()
            
    return epoch_loss / len(iterator)
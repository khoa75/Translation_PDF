import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import random
import math
import time

# Training functions would go here
def train(model, iterator, optimizer, criterion, clip):
    model.train()
    epoch_loss = 0
    
    for i, batch in enumerate(iterator):
        src = batch.src
        trg = batch.trg
        
        optimizer.zero_grad()
        
        output = model(src, trg)
        # output = [trg len, batch size, output dim]
        # trg = [trg len, batch size]
        
        output_dim = output.shape[-1]
        
        output = output[1:].view(-1, output_dim)
        trg = trg[1:].view(-1)
        # output = [trg len * batch size, output dim]
        # trg = [trg len * batch size]
        
        loss = criterion(output, trg)
        loss.backward()
        
        torch.nn.utils.clip_grad_norm_(model.parameters(), clip)
        optimizer.step()
        
        epoch_loss += loss.item()
        
    return epoch_loss / len(iterator)
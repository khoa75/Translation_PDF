import torch
import torch.nn as nn
import torch.nn.functional as F

class MultiHeadAttention(nn.Module):
    def __init__(self, hidden_size, num_heads, dropout):
        super().__init__()
        self.hidden_size = hidden_size
        self.num_heads = num_heads
        self.dropout = dropout
        
        self.query = nn.Linear(hidden_size, hidden_size)
        self.key = nn.Linear(hidden_size, hidden_size)
        self.value = nn.Linear(hidden_size, hidden_size)
        self.fc = nn.Linear(hidden_size, hidden_size)
        
        self.dropout_layer = nn.Dropout(dropout)
        
    def forward(self, query, key, value, mask=None):
        # Implementation of multi-head attention
        # query, key, value: [batch_size, seq_len, hidden_size]
        
        batch_size = query.shape[0]
        
        # Linear transformations
        Q = self.query(query)
        K = self.key(key)
        V = self.value(value)
        
        # Split into heads
        Q = Q.view(batch_size, -1, self.num_heads, self.hidden_size // self.num_heads).transpose(1, 2)
        K = K.view(batch_size, -1, self.num_heads, self.hidden_size // self.num_heads).transpose(1, 2)
        V = V.view(batch_size, -1, self.num_heads, self.hidden_size // self.num_heads).transpose(1, 2)
        
        # Scaled dot-product attention
        scores = torch.matmul(Q, K.transpose(-2, -1)) / torch.sqrt(torch.tensor(self.hidden_size // self.num_heads, dtype=torch.float32))
        
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e10)
        
        attention_weights = F.softmax(scores, dim=-1)
        attention_weights = self.dropout_layer(attention_weights)
        
        # Weighted sum of values
        output = torch.matmul(attention_weights, V)
        
        # Concatenate heads
        output = output.transpose(1, 2).contiguous().view(batch_size, -1, self.hidden_size)
        
        # Final linear layer
        output = self.fc(output)
        
        return output, attention_weights
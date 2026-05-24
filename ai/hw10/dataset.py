import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from transformers import AutoTokenizer

class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

def prepare_data(csv_path, model_name="distilbert-base-multilingual-cased"):
    df = pd.read_csv(csv_path)
    df = df.drop_duplicates().reset_index(drop=True)
    
    train_texts, test_texts, train_labels, test_labels = train_test_split(
        df["text"].tolist(), df["label"].tolist(), test_size=0.2, random_state=42
    )
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    train_encodings = tokenizer(train_texts, truncation=True, padding=True, max_length=128)
    test_encodings = tokenizer(test_texts, truncation=True, padding=True, max_length=128)
    
    train_dataset = CustomDataset(train_encodings, train_labels)
    test_dataset = CustomDataset(test_encodings, test_labels)
    
    return train_dataset, test_dataset, tokenizer
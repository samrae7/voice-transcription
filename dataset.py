import random
from torch.utils.data import Dataset
from datasets import load_dataset, load_dataset_builder


class AmiDataset(Dataset):
    def __init__(self, split="train", sample_rate=16000, segment_length = 30):
        super().__init__()
        self.ds = load_dataset("edinburghcstr/ami", "ihm", split=split, trust_remote_code=True)
        self.sample_rate = sample_rate
        self.segment_length = segment_length
    
    def __getitem__(self, index):
        sample = self.ds[index]
        audio = sample["audio"]
        waveform = audio["array"]
        sr = audio["sampling_rate"]
        
        if sr != self.sample_rate:
            raise ValueError(f"Expected sample rate {self.sample_rate}, but got {sr}")
        
        desired_samples = self.segment_length * self.sample_rate
        current_samples = waveform.size(-1)

            
        
        sub_interval_length = 1

    
    def __len__(self):
        return len(self.ds)
    
if __name__ == "__main__":
    # ihm - individual headet mic. sdm - single distant mic
    ds_builder = load_dataset_builder("edinburghcstr/ami", "ihm", trust_remote_code=True)
    print(f"desc: {ds_builder.info.description}")
    print(f"features: {ds_builder.info.features}")
    print(f"splits: {ds_builder.info.splits}")
    print("=====")
    split= 'train'
    ds = load_dataset("edinburghcstr/ami", "ihm", split=split, trust_remote_code=True)
    total_len = len(ds)
    print(f"\nTotal samples in {split} set: {total_len}")

    # Sample random indices
    # indices = random.sample(range(total_len), min(5, total_len))
    
    # Display samples
    print("\nExample samples:")
    print("===============")
    
    for idx in range(5):
        sample = ds[idx]
        print(f"\nSample {idx}:")
        print("------------")
        for key, value in sample.items():
            # Handle different types of values for better display
            if isinstance(value, (list, tuple)) and len(value) > 100:
                print(f"{key}: {type(value)} of length {len(value)}")
                print(f"First few elements: {value[:5]}...")
            else:
                print(f"{key}: {value}")

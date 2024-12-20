import random
from torch.utils.data import Dataset
from datasets import load_dataset, load_dataset_builder
import numpy as np

class AmiDataset(Dataset):
    def __init__(self, split="train", sample_rate=16000, segment_length = 30):
        super().__init__()
        self.ds = load_dataset("edinburghcstr/ami", "ihm", split=split, trust_remote_code=True)
        self.sample_rate = sample_rate
        self.segment_length = segment_length
        self.desired_samples = self.segment_length * self.sample_rate

        # This pointer tracks our position in the dataset
        self.current_idx = 0

    
    def __getitem__(self, index):
        accumulated_waveform = []
        total_samples = 0
        while total_samples < self.desired_samples and self.current_idx < len(self.ds):
            sample = self.ds[self.current_idx]
            audio = sample["audio"]
            waveform = audio["array"]
            sr = audio["sampling_rate"]
            
            if sr != self.sample_rate:
                raise ValueError(f"Expected sample rate {self.sample_rate}, but got {sr}")

            accumulated_waveform.append(waveform)
            total_samples += len(waveform)

            self.current_idx += 1
        
        # If we didn't reach 30s and no more data is available, just return what we have (or consider raising an error)
        if total_samples < self.desired_samples:
            raise IndexError("No more data available to form a segment.")
        
         # Concatenate all waveforms
        final_waveform = np.concatenate(accumulated_waveform)
        
        # At this point, final_waveform should be around 30 seconds
        return {
            "audio": final_waveform,  # np array of shape [samples]
            # You can also return text, labels, etc., if needed
        }

    
    def __len__(self):
        return len(self.ds)
    
if __name__ == "__main__":
    dataset = AmiDataset()

    # Example: Retrieve a few 30-second segments
    for i in range(3):
        item = dataset[i]
        print(f"Segment {i}: audio length in samples = {len(item['audio'])}, "
              f"duration = {len(item['audio']) / dataset.sample_rate} seconds")

import random
from torch.utils.data import Dataset
from datasets import load_dataset, load_dataset_builder
import numpy as np

from utils import validate_ami_dataset

class AmiDataset(Dataset):
    def __init__(self, split="train", sample_rate=16000, segment_length = 30):
        super().__init__()
        self.ds = load_dataset("edinburghcstr/ami", "ihm", split=split, trust_remote_code=True)
        self.sample_rate = sample_rate
        self.segment_length = segment_length
        self.desired_samples = self.segment_length * self.sample_rate

        # This pointer tracks our position in the dataset
        self.current_idx = 0
        self.meeting_id = self.ds[0]["meeting_id"]

    
    def __getitem__(self, index):
        accumulated_waveform = []
        total_samples = 0
        while total_samples < self.desired_samples and self.current_idx < len(self.ds):
            sample = self.ds[self.current_idx]
            audio = sample["audio"]
            waveform = audio["array"]
            sr = audio["sampling_rate"]
            meeting_id = sample["meeting_id"]
            # if meeting id changes, dont add any more segments
            if(meeting_id != self.meeting_id):
                self.meeting_id = meeting_id
                break
            
            if sr != self.sample_rate:
                raise ValueError(f"Expected sample rate {self.sample_rate}, but got {sr}")
            


            accumulated_waveform.append(waveform)
            total_samples += len(waveform)

            self.current_idx += 1
        
        if total_samples == 0:
            raise IndexError("No more data available to form a segment.")
        
        final_waveform = np.concatenate(accumulated_waveform)

        return {
            "audio": final_waveform,  # np array of shape [samples]
            # You can also return text, labels, etc., if needed
        }

    
    def __len__(self):
        return len(self.ds)
    
if __name__ == "__main__":
    dataset = AmiDataset()

    # validate_ami_dataset(31)

    # Example: Retrieve a few 30-second segments
    for i in range(3):
        item = dataset[i]
        print(f"Segment {i}: audio length in samples = {len(item['audio'])}, "
              f"duration = {len(item['audio']) / dataset.sample_rate} seconds"
              f"current_idx = {dataset.current_idx}"
              )

from datasets import load_dataset, load_dataset_builder

def validate_ami_dataset(num_samples=5):
    ###
    # This function is used to validate the dataset has loaded, and to print the first few samples
    ###
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
    
    for idx in range(num_samples):
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
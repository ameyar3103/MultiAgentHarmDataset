from datasets import load_dataset
from tqdm import tqdm
import subprocess  
import os 
import json
import tempfile
import time


logs_dir = "./logs/roundr2.0/PNA_finance"
os.makedirs(logs_dir, exist_ok=True)



with open("./PNA_finance.json", 'r') as f:
    data = json.load(f)

# print(data)


# AgentHarm
for i, task in tqdm(enumerate(data), total=len(data), desc="Processing Data Points"):
    # print("TASK: ", task)
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as temp_json:
        json.dump(task, temp_json)
        temp_json_path = temp_json.name  # Store file path

    log_file = f"{logs_dir}/PNA_finance_{i}.txt"

    with open(log_file, "w") as log:
        process = subprocess.Popen(
            ["python3", "trapi_gemini_roundr.py", "--json_data", temp_json_path],
            stdout=log,
            stderr=subprocess.STDOUT,
            text=True
        )

    process.communicate()       
    os.remove(temp_json_path)
    time.sleep(30)
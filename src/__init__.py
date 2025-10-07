import os

def scan_folder(root_dir):
    flow = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        rel_path = os.path.relpath(dirpath, root_dir)
        indent = "  " * (rel_path.count(os.sep))
        folder_name = os.path.basename(dirpath)
        flow.append(f"{indent}📁 {folder_name}/")
        for f in filenames:
            flow.append(f"{indent}  📄 {f}")
    return flow

if __name__ == "__main__":
    project_root = "."  # run this script from your project root
    structure = scan_folder(project_root)
    print("\n".join(structure))
    
    print("\n\n--- Summary Flow ---")
    # Optional: simple flow inference
    if os.path.exists("data/processed/cleaned_space_missions.csv"):
        print("1️⃣ Data Preprocessing done: data/processed/cleaned_space_missions.csv exists")
    if any(f.endswith(".py") for f in os.listdir("src")):
        print("2️⃣ Scripts available: src/ (data_preprocessing.py, eda_analysis.py, model.py, etc.)")
    if os.path.exists("models/space_mission_model.pkl"):
        print("3️⃣ Model trained: models/space_mission_model.pkl exists")
    if os.path.exists("deployment/app.py"):
        print("4️⃣ Deployment ready: deployment/app.py exists")

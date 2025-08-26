import json

notebook_path = "recipe_analysis.ipynb"  

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

if "widgets" in nb.get("metadata", {}):
    print("Removing metadata.widgets...")
    nb["metadata"].pop("widgets")

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=2)

print(f"✅ Fixed notebook saved: {notebook_path}")

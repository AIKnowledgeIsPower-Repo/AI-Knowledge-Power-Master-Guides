import os

def generate_roadmap():
    folder = './guides/'  # Folder name for English repo
    readme_file = 'README.md'
    
    if not os.path.exists(folder):
        print(f"[ERROR] Folder {folder} not found. Please create it.")
        return
            
    # Get sorted .md files
    guides = sorted([f for f in os.listdir(folder) if f.endswith('.md')])
    
    print(f"--- Updated Roadmap for English Repo ---")
    print("| Week | Guide Title | Category | Status |")
    print("| :--- | :--- | :--- | :--- |")
    
    for i, guide in enumerate(guides, 1):
        week = f"{i:02d}"
        # Format title: replace dashes with spaces and capitalize
        title = guide.replace('.md', '').replace('-', ' ').title()
        link = f"{folder}{guide}"
        status = "✅ Done"
        
        print(f"| {week} | [{title}]({link}) | AI & Tech | {status} |")

if __name__ == "__main__":
    generate_roadmap()

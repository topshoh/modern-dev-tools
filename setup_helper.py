import os

def setup_project():
    """
    Automatically creates the folder structure for the project.
    Helps new contributors start quickly.
    """
    folders = ['data', 'logs', 'scripts', 'docs']
    
    print("--- Starting Modern Dev Tools Setup ---")
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created folder: {folder}")
        else:
            print(f"Folder already exists: {folder}")
            
    print("\nSetup complete. Environment is ready for contributions!")

if __name__ == "__main__":
    setup_project()

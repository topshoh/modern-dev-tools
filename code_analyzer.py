import os

def analyze_code_quality(directory):
    """
    Script to analyze project structure and find empty files.
    Part of the Modern Dev Tools toolkit.
    """
    print(f"--- Analyzing directory: {directory} ---")
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith((".py", ".js", ".html", ".css")):
                file_path = os.path.join(root, file)
                size = os.path.getsize(file_path)
                status = 'OK' if size > 0 else 'Empty'
                print(f"File: {file} | Size: {size} bytes | Status: {status}")

if __name__ == "__main__":
    analyze_code_quality(".")
    print("\nAnalysis complete. Project is ready for AI-assisted optimization.")

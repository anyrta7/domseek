def load_domains(file_path):
    try:
        with open(file_path, 'r') as file:
            domains = [line.strip() for line in file.readlines() if line.strip()]
        return domains
    except FileNotFoundError:
        print(f"Error: file {file_path} not found!")
        return []
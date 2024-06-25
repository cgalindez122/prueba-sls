import subprocess

def get_last_deployment_commit_id():
    # Command to get the commit ID of the last commit on the main branch
    last_commit_command = "git rev-parse main"
    last_commit_id = subprocess.check_output(last_commit_command, shell=True).decode().strip()
    return last_commit_id

def get_changed_functions(base_ref):
    print("Base ref:", base_ref)
    # Get list of changed files compared to base_ref, including changes up to the current HEAD
    changed_files_command = ['git', 'diff', '--name-only', f'{base_ref}..HEAD']
    changed_files = subprocess.check_output(changed_files_command).decode().splitlines()
    print("Changed files:", changed_files)
    # Correctly filter and list files within 'functions' directory
    changed_functions_files = [file for file in changed_files if file.startswith('functions/')]
    return changed_functions_files

def main():
    base_ref = get_last_deployment_commit_id()  # Dynamically get the last deployment commit ID
    changed_functions = get_changed_functions(base_ref)
    # Output changed function names, space-separated
    print(' '.join(changed_functions))

if __name__ == '__main__':
    main()
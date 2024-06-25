import subprocess

def get_last_deployment_commit_id():
    # Command to get the commit ID of the last commit on the main branch
    last_commit_command = "git rev-parse main"
    last_commit_id = subprocess.check_output(last_commit_command, shell=True).decode().strip()
    return last_commit_id

def get_changed_functions(base_ref):
    print("Base ref:", base_ref)
    # Get list of changed files compared to base_ref
    changed_files = subprocess.check_output(['git', 'diff', '--name-only', base_ref]).decode().splitlines()
    print("Changed files:", changed_files)
    # Extract the unique directories of changed files
    changed_dirs = {file.split('/functions')[0] for file in changed_files}
    return changed_dirs

def main():
    base_ref = get_last_deployment_commit_id()  # Dynamically get the last deployment commit ID
    changed_functions = get_changed_functions(base_ref)
    # Output changed function names, space-separated
    print(' '.join(changed_functions))

if __name__ == '__main__':
    main()
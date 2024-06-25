import subprocess

def get_last_deployment_commit_id():
    # Example command to get the latest tag. Adjust according to your tagging strategy.
    # This command gets the latest tag by date.
    latest_tag_command = "git describe --tags `git rev-list --tags --max-count=1`"
    latest_tag = subprocess.check_output(latest_tag_command, shell=True).decode().strip()

    # Get the commit ID of the latest tag
    commit_id_command = f"git rev-list -n 1 {latest_tag}"
    commit_id = subprocess.check_output(commit_id_command, shell=True).decode().strip()
    return commit_id

def get_changed_functions(base_ref):
    # Get list of changed files compared to base_ref
    changed_files = subprocess.check_output(['git', 'diff', '--name-only', base_ref]).decode().splitlines()

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
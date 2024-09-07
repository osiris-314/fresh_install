import subprocess
import re
import os
from colorama import Fore

add_to_path_url = 'https://github.com/osiris-314/addtopath.git'

def install_dependencies():
    # Redirect stdout and stderr to /dev/null to suppress output
    print(Fore.LIGHTBLUE_EX + 'Updating The System ...' + Fore.RESET)
    subprocess.run('sudo apt update > /dev/null 2>&1',shell=True)
    #print(Fore.LIGHTBLUE_EX + 'Upgrading The System ...' + Fore.RESET)
    #subprocess.run('sudo apt upgrade -y > /dev/null 2>&1',shell=True)
    #print(Fore.LIGHTBLUE_EX + 'Installing Default Tools ...' + Fore.RESET)
    #subprocess.run('sudo apt install kali-linux-default -y > /dev/null 2>&1',shell=True)
    print(Fore.LIGHTBLUE_EX + 'Installing Packages ...' + Fore.RESET)
    result = subprocess.run(
        'sudo apt-get install ufw python3-dev libasound2-dev -y > /dev/null 2>&1', 
        shell=True, 
        check=True
    )
    if result.returncode != 0:
        print(Fore.RED + 'Error installing dependencies.' + Fore.RESET)
        exit(1)
    subprocess.run('sudo ufw enable > /dev/null 2>&1',shell=True)
    print('\n')
    print(Fore.LIGHTGREEN_EX + 'Firewall Enabled')
    print('\n')

def add_addtopath_to_path():
    match = re.search(r'https://github.com/([^/]+)/([^/]+)\.git', add_to_path_url)
    if match:
        result = match.group(2)
        repo_name = result
    print('Downloading Package: ' + Fore.LIGHTBLUE_EX + str(repo_name) + Fore.RESET)
    subprocess.run(f'git clone --quiet {add_to_path_url}', shell=True, check=True)
    subprocess.run(f'chmod +x {repo_name}/{repo_name}.py', shell=True, check=True)
    subprocess.run(f'sudo mv {repo_name}/{repo_name}.py /usr/local/bin/{repo_name}', shell=True, check=True)
    subprocess.run(f'rm -rf {repo_name}', shell=True, check=True)
    print(Fore.LIGHTGREEN_EX + 'Successfully Added ' + Fore.LIGHTBLUE_EX + str(repo_name) + Fore.LIGHTGREEN_EX + ' To The ' + Fore.YELLOW + 'PATH ' + Fore.RESET + '\n')

def check_file_exists(repo_name):
    return os.path.isfile(str(repo_name) + '/requirements.txt')

def add_other_to_path(url):
    match = re.search(r'https://github.com/([^/]+)/([^/]+)\.git', url)
    if match:
        result = match.group(2)
        repo_name = result
    print('Downloading Package: ' + Fore.LIGHTBLUE_EX + str(repo_name) + Fore.RESET)
    subprocess.run(f'git clone --quiet {url}', shell=True, check=True)
    if check_file_exists(repo_name):
        # Install requirements and suppress output
        print('Installing Requirements For ' + Fore.LIGHTBLUE_EX + str(repo_name) + Fore.RESET)
        result = subprocess.run(
            f'pip install -r {repo_name}/requirements.txt > /dev/null 2>&1', 
            shell=True
        )
        if result.returncode != 0:
            print(Fore.RED + f'Error installing requirements for {repo_name}.' + Fore.RESET)
            exit(1)
    subprocess.run(f'chmod +x {repo_name}/{repo_name}.py', shell=True, check=True)
    subprocess.run(f'addtopath -f {repo_name}/{repo_name}.py -c {repo_name}', shell=True, check=True)
    subprocess.run(f'rm -rf {repo_name}', shell=True, check=True)
    print('\n')

# Install dependencies and wait for it to complete
install_dependencies()
# Add 'addtopath' to the system path
add_addtopath_to_path()
# Process each repository
repos = [
    'https://github.com/osiris-314/rmfrompath.git',
    'https://github.com/osiris-314/capturehandshake.git',
    'https://github.com/osiris-314/netscan.git',
    'https://github.com/osiris-314/mitm.git',
    'https://github.com/osiris-314/decrypt.git',
    'https://github.com/osiris-314/encrypt.git',
    'https://github.com/osiris-314/monitormode.git',
    'https://github.com/osiris-314/exifextract.git',
    'https://github.com/osiris-314/exifremove.git',
    'https://github.com/osiris-314/datarecovery.git',
    'https://github.com/osiris-314/steganography.git',
    'https://github.com/osiris-314/shredder.git',
    'https://github.com/osiris-314/imageinstaller.git',
    'https://github.com/osiris-314/pico_rubber_ducky.git',
    'https://github.com/osiris-314/wifiaudit.git'
    'https://github.com/osiris-314/deauth.git'
]
for repo in repos:
    add_other_to_path(repo)
    

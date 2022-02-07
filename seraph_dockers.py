# seraph_docker.py 
# Author: @diveyez
import os
import sys
import time
#
import docker
#
# SP WAS BETTER THAN DOCKER CLI OUTS
import subprocess
#
def main():
    client, log_path = _set_up_environment()
    _run_docker_compose("docker-compose.yaml", log_path)
# BROKEN 
#
def _run_docker_compose(docker_compose_name, log_path):
    bash_command = f""docker-compose -f {docker_compose_name}} up -d"" # Tried f" string/cmd" and it did not work properly
    _execute_shell_command(bash_command, log_path)
# BROKEN 
#
# Works
def _execute_shell_command(bash_command, log_path):
    with open(log_path, "w") as output:
        subprocess.run(bash_command, shell=True,  # pass single string to shell, let it handle.
                stdout=output,stderr=output)
    while not output.closed:
        time.sleep(0.1)
    print(f"{os.linesep} COMMAND {bash_command} LOG OUTPUT:")
    with open(log_path, "r") as output:
        for line in output:
            print(line)
#
#
#
#  Useless Code Blocks Removed From Here
#
#
#
def _create_docker_log_file():
    log_location, log_name = "logs", "output.log"
    log_path = os.path.join(os.getcwd(), log_location, log_name)
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    assert os.path.isdir(os.path.dirname(log_path))
    if not os.path.isfile(log_path):
        os.mknod(log_path)

    return log_location, log_name, log_path


def _set_up_environment():
    log_location, log_name, log_path = _create_docker_log_file()
    client = docker.from_env()
    return client, log_path

if __name__ == "__main__":
    main()


import sys
import os
sys.path.append(os.path.join('..', '..', 'scripts'))
import base

def get_branch_name(directory):
    cur_dir = os.getcwd()
    os.chdir(directory)
    command = "git symbolic-ref --short -q HEAD"
    current_branch = base.run_command(command)['stdout']
    os.chdir(cur_dir)
    return current_branch


array_args = sys.argv[1:]
config = {}
for arg in array_args:
    if 0 == arg.find("--"):
        indexEq = arg.find("=")
        if -1 != indexEq:
            config[arg[2:indexEq]] = arg[indexEq + 1:]

branch = config["branch"] if "branch" in config else get_branch_name("../..")

print("---------------------------------------------")
print("build branch: " + branch)
print("---------------------------------------------")

modules = "desktop"

print("---------------------------------------------")
print("build modules: " + modules)
print("---------------------------------------------")

update = config["update"] if "update" in config else "1"

build_tools_params = ["--branch", branch,
                      "--module", modules,
                      "--update", update]
for conf_name in config:
    if conf_name == "branch" or conf_name == "module" or conf_name == "update":
        continue
    build_tools_params.append("--" + conf_name)
    build_tools_params.append(config[conf_name])

base.cmd_in_dir("..\\..", "python3", [".\\configure.py"] + build_tools_params)
base.cmd_in_dir("..\\..", "python3", [".\\make.py"])
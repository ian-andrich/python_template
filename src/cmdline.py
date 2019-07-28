import pathlib


if __name__ == "__main__":
    while True:
        print("Project Name:")
        project_name = input()
        if project_name == "":
            print("Invalid project name -- must not be an empty string")
        else:
            break
    print("Project source directory[./src]")
    cmd = input()
    if cmd == "":
        source_dir = pathlib.Path("./src/")
    else:
        source_dir == pathlib.Path(cmd)

    print("Documentation directory[./docs/]:")
    cmd = input()
    if cmd == "":
        docs_dir = pathlib.Path("./docs/")
    else:
        docs_dir == pathlib.Path(cmd)

    print("Tests dir[./tests/]:")
    cmd = input()
    if cmd == "":
        tests_dir = pathlib.Path("./tests/")
    else:
        tests_dir = pathlib.Path("cmd")



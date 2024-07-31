import os
import subprocess


def main() -> None:
    cwd: str = os.path.dirname(os.path.abspath(__file__))
    package_dir: str = os.path.abspath(os.path.join(cwd, ".."))
    cookiecutter_path: str = os.path.join(cwd, "cookiecutter")

    subprocess.check_call([cookiecutter_path, package_dir], shell=True)


if __name__ == "__main__":
    main()

from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:

    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        hypen_constat = '-e .'
        if hypen_constat in requirements:
            requirements = requirements.remove(hypen_constat)

    return requirements



setup (
    name = 'mlproject',
    version= '0.0.1',
    author = 'ArunSaiThunga',
    author_email = 'arunsaikumar.t@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt'),
)

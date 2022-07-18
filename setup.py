from typing import List
from setuptools import find_packages, setup
from typing import List


PROJECT_NAME = "housing-predictor"
VERSION = "0.0.2"
AUTHOR = "Rakesh H R"
DESCRIPTION = "This is my personal project with mocular coding"
PACKAGES = ['housing']
REQUIREMTN_FILE = "requirements.txt"


def get_Requirement_List()->List[str]:
    """
    Description : This function is going to return list of requirement mentioned in 
                  requirements.txt
    return : This function returns the list of name of libraries mentioned in 
                  requirements.txt
    """
    with open(REQUIREMTN_FILE) as file:
        return file.readlines().remove('-e .')

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(), #['housing']
    install_requires = get_Requirement_List()
)
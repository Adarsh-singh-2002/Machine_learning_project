from setuptools import setup,find_packages
from typing import List


# Declaring variables for setup functions.
PROJECT_NAME="housing-predictor"
VERSION="0.0.2"
AUTHOR="Adarsh Kumar"
DESCRIPTION="This is a end to end project on house price prediction."
#PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT="-e ."

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement mention in requirments.txt file

    return type of this funtion is going to return a list which contain name of the libraries mentioned in the requirements.txt file
    """

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    #packages=PACKAGES,
    packages=find_packages(),
    install_requires=get_requirements_list()
)


from setuptools import find_packages,setup
from typing import List
hipen_e = '-e .'

def get_requirements(file_path:str)->List[str]: #create the function
    '''
    This function returns the list of requirements
    '''
    requirements =[]

    with open(file_path) as file_obj: #open the file
        requirements = file_obj.readlines() #read the file line by line
        requirements=[req.replace('\n','') for req in requirements]
        if hipen_e in requirements:
            requirements.remove(hipen_e)
    return requirements


setup(
    name = 'mlproject',
    version= '0.0.1',
    author='Irfan',
    author_email= 'irfanalimatto72@gmail.com',
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt')

)
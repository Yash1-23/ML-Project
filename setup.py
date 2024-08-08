from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        for req in file_obj.readlines():
            req = req.strip()  # Remove leading/trailing whitespace
            if req and not req.startswith('-e') and not req.startswith('#'):
                requirements.append(req)
    return requirements
        
setup(
name = 'ML-project',
version='0.0.1',
author = 'Yash1-23',
author_email = 'yashwanthsinghgarandal@gmail.com',
install_requires = get_requirements('requirements.txt')
)
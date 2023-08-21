#Building the whole project as a package and can be uploaded into pypi and can be accessed by others as a package
from setuptools import find_packages,setup
#from typing import list

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str): #-> list[str]:
    '''

    this  function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() #whenever readlines will be called after each line it records \n so to remove it we use replace 
        requirements=[req.replace("\n"," ") for req in requirements] 

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



setup(

    name='mlproject',
    version='0.0.1',
    author='Bhanuprakash Vishwanadha',
    author_email='bhanu7795@gmail.com',
    packages=find_packages(),
   #we requries so many packages thats why not a good way -  install_requires=['pandas','numpy','seaborn'],
    install_requires=get_requirements('requirements.txt')
)
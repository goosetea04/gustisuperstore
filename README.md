# Assignment 2

## Explanation

1. How do you implement the checklists? Explain in a step-by-step manner
	1. We create a new Django project
 		- We first create a virtual environment by running the command:

      		`python3 -m venv env`

     		- To activate the virtual environment, we use:

       		`env\Scripts\activate.bat`

     		- I then made a text file named `requirements.txt` filled with dependencies needed for the project
   
         	- I then installed said dependencies with `pip install -r requirements.txt`
    
          	- Create a new Django project with the command, `django-admin startproject gustisuperstore`
    
          	- To ensure multiple hosts can access the project, add `"*"` to `ALLOWED_HOSTS` in `settings.py` to deploy
    
   		-I also added a `.gitignore` file to ensure that the deployment is smooth.

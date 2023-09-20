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
    
   		- I also added a `.gitignore` file to ensure that the deployment is smooth.
   
   2. We Created an app in the root directory named main by running the command `python manage.py startapp main`
  
   3. We then register the main app into the project by finding settings `settings.py` in gustisuperstore directory then finding `INSTALLED_APPS` and adding `main` to the code
  
   4. We Create a new directory that is called templates within main application. We then creare `main.html` inside the directory.
  
   5. Edit the `models.py` file inside the main application to define a new model. Edit th `models.py` to include name, amount, and description in the app.
  
   6. Create and apply model migrations.
  
   		- Run the code `python manage.py makemigrations` to create the migrations model

     		- Run the code  `python manage.py migrate` to use the model

   7. Edit `views.py`

		- Add the function `show_main` with `app`, `name`, and `class`, that is present in `main.html` that has beend modified by `{{ class }}` and `{{ name }}` on `main.html`

   8.  Configure URL routing in `urls.py` to map the function `views.py` to URL.

		- Import configs

   		- Add app_name = 'main' into the urls.py
   9. Do the four git mantras (pull, add, commit, push) to push into github
  
   10. Deploy
  
2. Create a diagram explaining the flow of client requests to a Django web app and its response. Also in the diagram, explain the connections between urls.py, views.py, models.py, and the HTML file(s).


3. What is the purpose of a virtual environment? Can we create a Django web app without a virtual environment?

Virtual environments help developers by providing an isolated environments between projects with each project having their own dependencies and Python version. This ensures that each app can be replicated with the required dependencies, libraries and version. It is possible to run Django without env, but this will mean that configurations will be global and this may cause problems.

4. What is MVC, MVT, and MVVM? Explain the differences between them?

To start, MVC is the most widely used architecture. What it does is separate the application into three main components that are **model,** **view** and **controller**. MVT is another architecture that is a variation of MVC. One example is Django. MVVM is an architecture that is used for mobile development. It is divided into **model,** **view,** and **viewmodel**. A major difference between the three is that MVT's controller component is taken care of by the framework. MVVM handles more with graphical user interfaces. The main differentating factor between the three is the mediator component entry to the application.

---

# Assignment 3

1. What is the difference between POST form and GET form in Django?
   
   	- In Django and other web development, the two main methods for *submitting* data are **POST** and **GET**. The difference in these methods dictates how the data is sent to the server and how it can be processed.

   	- The GET method appends form data to the URL as query parameters. It is used for requests that retrieve data from the server but are not really used for large amounts of data; furthermore, some data is present in the URL, so it should be used cautiously so as to not get any data in the URL. Since it is a URL, it has URL length limitations.
  
   	- The POST method sends for data in the body of the HTTP request. It is used to requests that modify data on the server and is used for sending larger data. Since data is not visible in the URL, it is much more secure. It does not have the same character limitations as the GET method.
   	  
2. What are the main differences between XML, JSON, and HTML in the context of data delivery?
3. Why is JSON often used in data exchange between modern web applications?
4. Explain how you implemented the checklist above step-by-step (not just following the tutorial).

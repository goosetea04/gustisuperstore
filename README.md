# Assignment 2

## Explanation

1. ### How do you implement the checklists? Explain in a step-by-step manner
	1. We create a new Django project
 		- We first create a virtual environment by running the command: `python3 -m venv env`. To activate the virtual environment, we use: `env\Scripts\activate.bat`

     		- I then made a text file named `requirements.txt` filled with dependencies needed for the project. I then installed said dependencies with `pip install -r requirements.txt`
    
          	- Create a new Django project with the command, `django-admin startproject gustisuperstore`
    
          	- To ensure multiple hosts can access the project, add `"*"` to `ALLOWED_HOSTS` in `settings.py` to deploy. I also added a `.gitignore` file to ensure that the deployment is smooth.
   
	2. We Created an app in the root directory named main by running the command `python manage.py startapp main`
  
	3. We then register the main app into the project by finding settings `settings.py` in gustisuperstore directory then finding `INSTALLED_APPS` and adding `main` to the code
  
	4. We Create a new directory that is called templates within main application. We then create `main.html` inside the directory.
  
	5. Edit the `models.py` file inside the main application to define a new model. Edit the `models.py` to include name, amount, and description in the app.
  
	6. Create and apply model migrations.
  
   		- Run the code `python manage.py makemigrations` to create the migrations model

     		- Run the code  `python manage.py migrate` to use the model

	7. Edit `views.py`

		- Add the function `show_main` with `app`, `name`, and `class`, which is present in `main.html` that has beend modified by `{{ class }}` and `{{ name }}` on `main.html`

	8.  Configure URL routing in `urls.py` to map the function `views.py` to URL.

		- Import configs

   		- Add app_name = 'main' into the urls.py
   
	9. Do the four git mantras (pull, add, commit, push) to push into github
  
	10. Deploy
  
2. ### Create a diagram explaining the flow of client requests to a Django web app and its response. Also in the diagram, explain the connections between urls.py, views.py, models.py, and the HTML file(s).


3. ### What is the purpose of a virtual environment? Can we create a Django web app without a virtual environment?

Virtual environments help developers by providing an isolated environments between projects with each project having their own dependencies and Python version. This ensures that each app can be replicated with the required dependencies, libraries and version. It is possible to run Django without env, but this will mean that configurations will be global and this may cause problems.

4. ### What is MVC, MVT, and MVVM? Explain the differences between them?

To start, MVC is the most widely used architecture. What it does is separate the application into three main components that are **model,** **view** and **controller**. MVT is another architecture that is a variation of MVC. One example is Django. MVVM is an architecture that is used for mobile development. It is divided into **model,** **view,** and **viewmodel**. A major difference between the three is that MVT's controller component is taken care of by the framework. MVVM handles more with graphical user interfaces. The main differentating factor between the three is the mediator component entry to the application.

---

# Assignment 3

1. ### What is the difference between POST form and GET form in Django?
   
   	- In Django and other web development, the two main methods for *submitting* data are **POST** and **GET**. The difference in these methods dictates how the data is sent to the server and how it can be processed.

   	- The GET method appends form data to the URL as query parameters. It is used for requests that retrieve data from the server but are not really used for large amounts of data; furthermore, some data is present in the URL, so it should be used cautiously so as to not get any data in the URL. Since it is a URL, it has URL length limitations.
  
   	- The POST method sends for data in the body of the HTTP request. It is used to requests that modify data on the server and is used for sending larger data. Since data is not visible in the URL, it is much more secure. It does not have the same character limitations as the GET method.
   	  
2. ### What are the main differences between XML, JSON, and HTML in the context of data delivery?

   	Before we start, lets get to know `XML`, `JSON`, and `HTML`.

   	**XML** stands for extensible mark-up language. It is designed for carrying out data. This also allows XML able to process more complex data structures suchh as trees or graphs. It focuses more on generality, usability and simplicity. **JSON** stands for JavaSCript Object Notation and it is a format for store and sending data from a server to a webpage. It represents its data as dictionary style key-value pairs and this makes it easy to understand. Lastly, we have **HTML** or Hyper Text Markup-Language. This is a language that is used to mae webpages; furthermore, it is used to define structures and add interactivity on the page.

   	Only `XML` and `JSON` operates similarlyy as in they both are used in data transmission. `HTML` is used for describing and displaying data.
   	
3. ### Why is JSON often used in data exchange between modern web applications?

   	JSON is most often used in data echange due to some advantages it have and conveniece it provides to users. Among them are:

   	- JSON is **lightweight and human-readable**. Its syntax resembles the way objects are defined in JavaScript, making it intuitive for developers to understand.
   	- JSON can be **easily parsed** and generated in a huge majority of programming languages. Most languages nowadays have built-in libraries that can be installed easily. This makes it convenient for developers.
   	- The **data transfer** of JSON is more compact compared to something like XML. This means it requires less bandwidth for data transmission, which can lead to faster load times and better performance in web applications
	- JSON supports a **wide range of data types,** including objects, arrays, strings, numbers, booleans, and null values. This flexibility allows for complex data structures to be represented, making it suitable for a variety of data exchange scenarios.
  
   	Among many other reasons, these are just some reasons why JSON is most often used in Data Transmission.
   	  
4. ### Explain how you implemented the checklist above step-by-step (not just following the tutorial).

	1. Create a form input to add a model object to the previous app.
    
		-Before doing anything, I used visual studio code which is an IDE wherein I edited all of the files needed for this assignmenet.
		- In the `root` directory, I made a folder named `templates` and made a file named `base.html`. Here, I added HTML code that serves as the base of my webpage.

		- The contents of the file I got from the documentation of tutorial 2. I have a project folder named `gustisuperstore` and here, I edited the `settings.py` and edited `TEMPLATES` so that it can detect the html.

		- Inside `main` folder, I edited `main.html` so that it can implemebt the basic structure.

 		-Now I will make the forms! Inside the `main` folder, I made a new file named `forms.py`


 	2. Add 5 views to view the added objects in HTML, XML, JSON, XML by ID, and JSON by ID formats and create the URLS for each of them

		The HTML view was created in the previous step, but what about the others? For XML, I navigated back to the `views.py` file, imported the necessary components, and created a new function called `show_xml` with a `request` parameter. After that, I added a return statement to provide the response as an XML format. Moving on to the `urls.py` file, I imported this function and included it in the `urlpatterns` to ensure it is correctly routed in the URL.

		I followed a similar process for handling JSON, with the only difference being the function name. As for handling ID formats, it largely mirrors the previous steps. However, I adjusted the `data` variable to retrieve information based on a specific ID using `Product.objects.filter(pk=id)`. This enables the ability to search for items using an ID address.

	3. Access the five URLs in point 2 using Postman, take screenshots of the results in Postman, and add them to README.md.






   

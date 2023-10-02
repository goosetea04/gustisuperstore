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

<img src="/assets/Diagram.PNG">

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

 		- Now I will make the forms! Inside the `main` folder, I made a new file named `forms.py`

		- I then imported some components that are `ModelForm` and `Product`. Product itself is called on from `models.py`.
		- In `views.py` I imported `HttpResponseDirect`, `reverse`, `Product` and `ProductForm`. These respectively have the usages of: processing responses,  retrieving URL, implementing data, and creating the form.

		- Still in `views.py,` I made a function called `create_product` that, after a form with a product, price and description is made, renders it onto the website.

		- I edited the `show_main` function so that I am able to process and fetch the data.

 		- I then opened `urls.py` and imported the `create_product` function I just made! I also added it to the path in `urlpatterns`.

		- In the `templates` sub directory, I created `create_product.html` that implements the `POST` method from `django` to render a table display.

		- Finally, I implemented `create_product.html` so that it can be displayed on the page.


 	3. Add 5 views to view the added objects in HTML, XML, JSON, XML by ID, and JSON by ID formats and create the URLS for each of them

		- I navigated back to the `views.py` file, imported the necessary components, and created a new function called `show_xml` with a `request` parameter. After that, I added a return statement to provide the response as an XML format. Moving on to the `urls.py` file, I imported this function and included it in the `urlpatterns` to ensure it is correctly routed in the URL.

		- I followed a similar process for handling JSON, with the only difference being the function name. As for handling ID formats, it largely mirrors the previous steps. However, I adjusted the `data` variable to retrieve information based on a specific ID using `Product.objects.filter(pk=id)`. This enables the ability to search for items using an ID address.

	4. Access the five URLs in point 2 using Postman, take screenshots of the results in Postman, and add them to README.md.

<img src="/assets/PIC 1.png">
<img src="/assets/PIC 2.png">
<img src="/assets/PIC 3.png">
<img src="/assets/PIC 4.png">
<img src="/assets/PIC 5.png">

---

# Assignment 4

1. ### What is UserCreationForm in Django? Explain its advantages and disadvantages.
   
	In Django, UserCreationForm is a built-in form provided by the Django authentication framework that simplifies the process of creating a new user. It is designed to be used in conjunction with the Django authentication system to handle user registration and account creation. Some advantages and disadvantages include.

	## Advantages

	- It seamlessly integrates with Django's built-in authentication system, which includes features like password hashing, session management, and user authentication.
	- `UserCreationForm` provides a pre-built form with fields like username, password, and confirmation, making it quick and easy to set up user registration functionality.
	- By using `UserCreationForm`, we maintain a consistent user creation process across your application, which can enhance the user experience.
	- `UserCreationForm` incorporates built-in security measures like password validation and password hashing, helping to ensure that user accounts are created securely.

	## Disadvantages

	- The default `UserCreationForm` includes basic fields like username and password. If you need to collect additional information during user registration, you'll need to extend or customize the form.
	- For very specific or complex user registration processes, UserCreationForm might not cover all the required functionalities. In such cases, developers may need to build a custom registration form from scratch.
	- While the form logic is provided, the styling and UI design are not. Developers will still need to implement the front-end design and style the form to fit the application's aesthetic.   

2. ### What is the difference between authentication and authorization in Django application? Why are both important?

	- Authentication is the process of verifying the identity of a user, system or process. It esseentially asks the question, "Who are you?" In Django, authentication involves confirming that a user is who they claim to be. This is typically done by checking their credentials, such as a username and password. Django provides a built-in authentication system that handles user authentication, including features like session management, password hashing, cookie tracking,  and user registration.
	- Authorization is the process of determining what actions a user is allowed to perform within a system or application. It answers the question, "What are you allowed to do?" In Django, authorization involves defining permissions and access controls for different parts of the application. This can include specifying which users or groups of users have the right to view, create, edit, or delete certain resources.

	I believe that both are important due to the nature of authentication being crucial to keeping a system safe. Authentication and Authorization work in tandem to ensure the django app is secure. Authentication helps make sure that the right person can use the app, and authorization ensures that the person using the app has the right acces to potentially sensitive info.

3. ### What are cookies in website? How does Django use cookies to manage user session data?

	Cookies are small pieces of data that websites store on a user's browser. They are used to remember information about the user's interactions with the site. When a user visits a website, the server sends a cookie to the browser, which is then stored locally. The browser includes this cookie in subsequent requests to the same website, allowing the server to retrieve and use that information.

	In Django, cookies are used for session management, where cookies are used to track session. They help the server recognize a user as they navigate through the site. They also help with personalization, authentication and remembering user choices. Essentially, if a command tracks attributes to users, then cookies would most liekly be used.
    
6. Are cookies secure to use? Is there potential risk to be aware of?

	Cookies are a fundamental part of web browsing and are generally considered secure when used properly. However, there are potential risks and security considerations that developers and website owners should be aware of:

	- There may be cookie size limitations, that when we are expanding the app, the cookie size may expand. This may cause problems in the future.
	-  Session cookies are stored temporarily and are deleted when the user closes their browser. Persistent cookies, on the other hand, have an expiration date. Developers should carefully consider the lifespan of cookies to balance convenience and security.
	- Avoid storing sensitive information directly in cookies. Instead, it's recommended to store references (like session IDs) and keep the actual data on the server. Even if a cookie is intercepted, the attacker won't have direct access to sensitive information.

	Overall,  cookies are generally secure when used with best practices and appropriate security measures. However, developers should be aware of potential risks and take steps to mitigate them.

8. Explain how you implemented the checklist above step-by-step (not just following the tutorial).

1. I first opened `views.py` inside `main` folder and imported `redirect`, `UserCreationfForm`, and `messages`. I then made a function called `register` that accepts `requests` as a parameter.

```py
	def register(request):
	form = UserCreationForm()

	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
        		form.save()
        		messages.success(request, 'Your account has been successfully created!')
        		return redirect('main:login')
	context = {'form':form}
	return render(request, 'register.html', context)
```
2.  I then made a file called `register.html` inside `templates` inside `main`. After that, I added routing.

 ```py
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
3. I then made a log out function witthin `views.py` inside the `main` folder.
4. I still made routing inside `views.py`.
5. Don't forget to restrict acces to the main page by importing the code. `from django.contrib.auth.decorators import login_required ` and adding the code,
   
```py
	show_main: @login_required(login_url='/login')
```

6. Don't forget to modify the `login_user` function to better reflect the chqanges we made.
7. Inside `show_main`, add the new variable `last_login` by writing `'last_login": request.COOKIES["last_login"]`
8. Fix the `logout_user` function so that our webapp will remove cookies after user logout by writing `response.delete_cookie('last_login')`
9. Import user that was made to `models.py`
10. Modify `Product` to add
```py
	class Product(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
```
Modify `show_main` and `create_products` function so that it connects user id qit user product

### We Are Done!!!

the last thing we need to do is make migrations and run our server!

`python manage.py makemigrations`
`python manage.py migrate`
`python manage.py runserver`

---
# Assignment 5

## Explain the purpose of some CSS element selector and when to use it.

1. Universal Selector (*):
	- What it does is select all elements on a page. It is, however, rarely used on its own, and it is mostly used in or helps with global changes or resets.
	``` py
 	* {
	    margin: 0;
	    padding: 0;
	}
	```

2. Tag Selector (div) (p) (h1):
	- We use this when we want to select HTML elements based on their tag name i.e: div, p, h1. We use it when we want to apply a style to all instances of a particular HTML element.
	```py
 	p {
		font-size: 16px;
		color: #333;
	}
	```

3. Class Selector (.classname):
	- We use it to select elements with a specific attribute. We use it when we want to change the design of elements that share a common class.
	``` py
 	.highlight {
    		background-color: yellow;
	}
 	```

## Explain some of the HTML5 tags that you know.

1. ### header:
	This tag is used to define the header in the webpage. The header typically includes navigation, titles and introductory elements to the user of a webpage.
2. ### nav:
	This tag contains navigation links for a document. It's used to define the navigation menu, which typically includes links to different sections or pages of a website.
3. ### section:
	Defines a thematic grouping within a document. It's used to organize content into distinct sections, each with its own heading.
4. ### footer:
	Defines a footer section for a document or a section within a document. It typically contains information about the author, copyright, and links to related documents.

## What are the differences between margin and padding?

Margin and padding are two fundamental concepts in CSS (Cascading Style Sheets) that control the spacing and layout of elements on a web page. They serve different purposes and are applied in distinct ways -> Margin is the space outside an element, controlling its positioning in relation to other elements, while padding is the space inside an element, influencing the distance between its content and border.

- Margin is the space outside of an element, usually found between its border and adjacent elements. This controls the gap between elements. The margin also creates an "invisible" area around the element which cannot be used for content or background. Sometimes margins can also have a negative value meaning that they can overlap elements.

- On the other hand, Padding is the space **_inside_** an element. This means the space between its content and its border. It controls the space around the content within an element. We can think of padding as a designated area within an element where we can place content. padding cannot have negative values like margins do.

## What are the differences between the CSS framework Tailwind and Bootstrap? When should we use Bootstrap rather than Tailwind, and vice versa?

### Some key differences between Tailwind and Bootstrap include:

- Tailwind follows a utility-first approach where you build components  by applying small utility classes directly in your HTML. It provides a wide range of low-level utility classes that you can combine to create custom designs. On the other hand, Bootstrap offers a component-based approach, providing pre-designed, styled-components that you can use in your project. It encourages consistency through its predefined component library.

- Tailwind is highly customizable, allowing you to build designs from the ground up with utility classes and configure the framework to suit your specific needs. Bootstrap offers some level of customization through Sass variables, but it's primarily designed to be used as a complete package.

- Tailwind contains a vast set of utility classes hence making it generally have a larger file size. Bootstrap Provides a comprehensive set of components, which can lead to a larger initial file size, but you have the option to customize and only include the components you use, making the file size smaller.

As for when to use Tailwind and Bootstrap:

- We use Tailwind when we prefer a utility-first approach and control over our design or someone who wants to build a highly-customized and unique design.

- We use Bootstrap when we want to quuickly build a Django webapp that comes equipped with pre-designed components. We also use Bootstrap when we prefer a modular, component-based approach to development. Lastly, we use Bootstrap when we are prioritizing speed as the most important factor of development.

### Explain how you implemented the checklist above step-by-step (not just following the tutorial).



   

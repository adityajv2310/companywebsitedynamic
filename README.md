# Dynamic Website Design for a Manufacturing Company
## AIM:
To design a dynamic website for a chip manufacturing company.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 7:
Create a database model and migrate the database.
### Step 8:
Retrieve data from database and display it in a dynamic webpage.
### Step 9:
Publish the website in the given URL.

## PROGRAM:

### products.html
~~~
{% extends "dynamicwebsite/base1.html" %}

{% block content %}
    <div class="productcontent">    
    <h1>Our Premium Products</h1>
    <div class="productitems">
        {% for products in products %}
        <div class="productitem"> 
            <div class="itemimage">
            <img src="{{ products.photo.url }}" alt="Product Photo">
            </div>
            <div class="itemname">{{ products.itemname }}</div>
            <div class="itemprice">{{ products.itemprice }} </div>
        </div>
        {% endfor %}
    </div>
    </div>
{% endblock  %}
~~~

### people.html
~~~
{% extends "dynamicwebsite/base1.html" %}

{% block content %}
    <div class="peoplecontent">
    <h1>Our Team</h1>
    <div class="crewmembers">
        {% for people in peoples %}
        <div class="crewmember">
            <div class="memberimage">
                <img src="{{ People.photo.url }}" alt="People Photo" style="width:200px;height:200px;">
            </div>
            <div class="membername">{{ people.membername }}</div>
            <div class="designation">{{ people.designation }}</div>
        </div>
        {% endfor %}
    </div>
    </div>
{% endblock  %}
~~~

### views.py
~~~
from django.shortcuts import render
from .models import Products
from .models import People

# Create your views here.

def home(request):
    context = {}
    return render(request, 'dynamicwebsite/home.html', context)

def products(request):
    context = {}
    context["products"] = Products.objects.all()
    return render(request, 'dynamicwebsite/products.html', context) 

def people(request):
    context = {}
    context["people"] = People.objects.all()
    return render(request, 'dynamicwebsite/people.html', context)

def contactus(request):
    context = {}
    return render(request, 'dynamicwebsite/contactus.html', context)
~~~




## OUTPUT:
![output](./static/img/ot1.png)
![output](./static/img/output3.png)
![output](./static/img/output4.png)
![output](./static/img/output5.png)
![output](./static/img/output6.png)
![output](./static/img/output8.png)
![output](./static/img/output9.png)
![output](./static/img/output10.png)

## RESULT:
Thus a dynamic website is designed for the chip manufacturing company and is hosted in the URL http://adityajv.student.saveetha.in:8000/. HTML code is validated.
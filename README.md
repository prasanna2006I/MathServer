# Ex.05 Design a Website for Server Side Processing
## Date:20-03-2024

## AIM:
To design a website to find surface area of a Right Cylinder in server side.

## FORMULA:
Surface Area = 2Πrh + 2Πr<sup>2</sup>
<br>r --> Radius of Right Cylinder
<br>h --> Height of Right Cylinder

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
### MATH
```HTML
<head>
   
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    
    <title>SURFACE AREA OF CYLINDER</title>

    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <style type="text/css">

        body {
            background-color:rgb(218, 245, 10);
        }

        .edge {
            display: flex;
            height: 100vh;
            width: 100%;    
            justify-content: center;
            align-items: center;
        }

        .box {
            display: block;
            width: 550px;
            min-height: 300px;
            font-size: 20px;
            background-color: rgb(3, 217, 255);
            border-radius: 10px;
            box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
        }

        .formelt {
            color:black;
            text-align: center;
            margin-top: 7px;
            margin-bottom: 6px;
        }

        h1 {
            color:rgb(0, 0, 0);
            text-align: center;
            padding-top: 20px;
        }
        input{
            margin: 5px;
            padding: 5px;
            border-radius: 5px;
            border: none;

        }
    </style>
</head>

<body>
    <div class="edge">
        <div class="box">
             <h1>PRASANNA I (212223220079)</h1>
            <h1>Surface Area of Cylinder </h1>

            <form method="POST">
                {% csrf_token %}
                <div class="formelt">
               Radius : <input type="text" name="radius" value="{{r}}"></input>(in m)<br/>
                </div>
                <div class="formelt">
                Height : <input type="text" name="height" value="{{h}}"></input>(in m)<br/>
                </div>
                <div class="formelt">
                <input type="submit" value="Calculate"></input><br/>
                </div>
                <div class="formelt">
                Area : <input type="text" name="area" value="{{area}}"></input>m<sup>2</sup><br/>
            </form>
        </div>
    </div>
</body>
</html>
```
### VIEWS.PY
```HTML
from django.shortcuts import render
def cylinarea(request):
    context = {}
    context['area'] = "0"
    context['r'] = "0"
    context['h'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        print('request.POST:', request.POST)
        r = request.POST.get('radius', '0') 
        h = request.POST.get('height', '0') 
        print('radius =', r)
        print('height =', h)
        area = 2 * 3.14 * int(r) * int(h) + 2*3.14*int(r)*int(r)
        context['area'] = area
        context['r'] = r
        context['h'] = h
        print('Area =', area)
    
    return render(request, 'mathapp/math.html',context)
```
### URLS.PY
```HTML
from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('surfaceareaofcylinder/',views.cylinarea,name="surfaceareaofcylinder"),
    path('',views.cylinarea,name="surfaceareaofcylinder")
]

```

## SERVER SIDE PROCESSING:
![alt text](<Screenshot 2024-04-28 165129.png>)

## HOMEPAGE:
![alt text](<Screenshot 2024-04-28 164815.png>)

## RESULT:
The program for performing server side processing is completed successfully.

from django.http import HttpResponse
from django.shortcuts import render

#dummy posts list

posts = [

    {
        "id":1,
        "title": 'Let\'s explore python',
        "content": 'Python is a high-level, interpreted programming language known for its simplicity and readability, making it a popular choice for both beginners and experienced developers. Python emphasizes code readability with its clean syntax, which allows developers to express concepts in fewer lines of code compared to languages like Java or C++. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python’s extensive standard library and a vast ecosystem of third-party packages make it ideal for a wide range of applications, from web development and data analysis to machine learning and automation.'
    }, {
        "id":2,
        "title": 'Let\'s explore java',
        "content": 'Java is a versatile, object-oriented programming language designed to have as few implementation dependencies as possible. It is known for its portability across platforms, thanks to the Java Virtual Machine (JVM) that allows Java programs to run on any device or operating system that supports the JVM. Java is statically typed, meaning that type checking is performed at compile-time, which helps in catching errors early in the development process. Java is widely used in large-scale enterprise applications, Android app development, and distributed computing, and it remains a critical language for server-side applications.'
    }, {
        "id":3,
        "title": 'Let\'s explore php',
        "content": 'PHP (Hypertext Preprocessor) is a server-side scripting language primarily used for web development. It is embedded within HTML, making it an accessible option for creating dynamic web pages and applications. PHP is open-source, easy to learn, and integrates well with databases like MySQL, which has contributed to its widespread use in content management systems like WordPress and Drupal. Despite the rise of newer technologies, PHP continues to power a significant portion of the web, thanks to its continuous updates, active community, and adaptability in creating scalable web solutions.'
    }
]



# Create your views here.

def viewname(request):
    html = ""
    for post in posts:
        html += f'''
            <div>
                <h1>{post['id']} - {post['title']}</h1>
                <p>{post['content']}</p>
            
            </div>    
'''
    return HttpResponse(html)
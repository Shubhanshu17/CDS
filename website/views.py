from django.http import HttpResponse

def home_page(request):
    return HttpResponse('''
<p style='text-align : center ; color : blue ; background-color : black ; font-size : 30px'>Home Page Of Site</p>
''')

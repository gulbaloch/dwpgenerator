from django.shortcuts import render
from django.http import HttpResponse

def about_page_generator(request):
    if request.method == 'POST':
        website_name = request.POST.get('website_name')
        website_type = request.POST.get('website_type')
        website_specialty = request.POST.get('website_specialty')
        about_page_content = f"<h1>About Us</h1><p>Welcome to {website_name}, your premier destination for {website_type}. Our specialty lies in {website_specialty}. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut lacus vel velit ultricies vestibulum.</p>"
        return render(request, 'about_page_generator.html', {'about_page_content': about_page_content})
    return render(request, 'about_page_generator.html')

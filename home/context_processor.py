from home.views import about, contact

def navigation(request): 
    contact = contact.objects.all()
    home = home.objects.all()
    about = about.objects.all()
   
    
    # category = Category.objects.all()
    return {
        "contact": contact,
        "home": home,
        "about": about,
        # "category": category,
     }

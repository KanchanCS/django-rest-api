from django.http import HttpResponse, JsonResponse


def home_page(request):
    print("home page ")
    friend = ["kanchan", "shalu", "jon"]
    return JsonResponse(friend, safe=False)

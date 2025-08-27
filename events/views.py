import base64
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render

last_event = {
    'name': None,
    'surname': None,
    'image_base64': None,
}

@csrf_exempt
def receive_event(request):
    global last_event

    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        image = request.FILES.get('image')

        img_b64 = None
        if image:
            img_b64 = base64.b64encode(image.read()).decode('utf-8')

        last_event['name'] = name
        last_event['surname'] = surname
        last_event['image_base64'] = img_b64

        return HttpResponse("OK")

    # GET — oxirgi eventni ko'rsatish
    return render(request, 'events/show.html', {
        'name': last_event['name'],
        'surname': last_event['surname'],
        'image_base64': last_event['image_base64'],
    })

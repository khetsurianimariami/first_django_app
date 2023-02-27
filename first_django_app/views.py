from django.http import HttpResponse


def hello(request):
    body = """
    <h1 style="color:red;font-family:'Courier New';text-align:center;">
    gamarjoba mariam
    </h1>
    """

    return HttpResponse(body)


def hello_specific(request, name: str):
    body = f"""
    <h1 style="color:red;font-family:'Courier New';text-align:center;">
    gamarjoba {name}
    </h1>
    """

    return HttpResponse(body)

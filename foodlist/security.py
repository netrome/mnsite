

def is_safe(form):
    data = form.cleaned_data

    fields = [data["name"], data["description"]]

    for text in fields:
        if "<" in text:
            print("Found malicious code!!!")
            return False
    return True

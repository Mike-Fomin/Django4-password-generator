from django.shortcuts import render
import random
import string


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    chars = list(string.ascii_lowercase.replace('i', '').replace('l', '').replace('o', ''))
    the_password = [random.choice(chars)]
    choices = 1

    if request.GET.get('uppercase'):
        up_chars = string.ascii_uppercase.replace('I', '').replace('O', '')
        chars.extend(list(up_chars))
        the_password.append(random.choice(up_chars))
        choices += 1
    if request.GET.get('digits'):
        digs = string.digits.replace('0', '').replace('1', '')
        chars.extend(list(digs))
        the_password.append(random.choice(digs))
        choices += 1
    if request.GET.get('specials'):
        specs = '!-+*?^%&#='
        chars.extend(list(specs))
        the_password.append(random.choice(specs))
        choices += 1

    length = int(request.GET.get('length', 8))

    for _ in range(length - choices):
        the_password.append(random.choice(chars))
    random.shuffle(the_password)
    the_password = ''.join(the_password)

    return render(request, 'generator/password.html', {'password': the_password})


def about(request):
    return render(request, 'generator/about.html')

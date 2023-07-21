from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    print("index function entered !!!!!!!!!!!!")
    return render(request, "index.html")

def pets_logout(request):
    print("logout function entered !!!!!!!!!!!!")
    logout(request)
    return redirect('index')
    

def pets_login(request):
    print("login function entered !!!!!!!!!!!!")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"username={username}. passowrd={password}")

        # Authenticate the user - validating user password. return user object if valid
        user = authenticate(request, username=username, password=password)
        print(f"authenticate passed. user is:{user}")

        if user is not None:
            # If the credentials are correct, log in the user
            login(request, user)
            print(f"** login passed. user is:{user}")
            return redirect('playlist')
        else:
            print(f"!! error login. user is:{user}")
            # If authentication fails, show an error message or redirect back to the login page
            error_message = "Invalid credentials. Please try again."
            return render(request, 'index.html', {'error_message': error_message})

    return redirect('index')

@login_required
def playlist(request):
    print("playlist function entered !!!!!!!!!!!!")
    # bring playlist for this user from database
    print(f"CURRENT USER IS: {request.user}")
    # user.playlist_set.all()
    return render(request, "playlist.html")


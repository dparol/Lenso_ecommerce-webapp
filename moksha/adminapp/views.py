from django.shortcuts import render



# # Create your views here.


# def user_logout(request):
#     logout(request)
#     return redirect('admin_home')


# def admin_index(request):
#     return render(request,'admin_index.html')



# def admin_home(request):
#     return render(request,'admin_home.html')


# def admin_user_login(request):

#     if request.user.is_authenticated:
#         return redirect('admin_index') 

#     if request.method == 'POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user=authenticate(request,username=username,password=password)
        
#         if user is not None:
#             if user.is_superuser:
#                 login(request,user)
#                 return redirect('admin_index')
           
        
#         else:
#             message.info(request,'enter a valid username or password')
#     return render(request,'login.html')
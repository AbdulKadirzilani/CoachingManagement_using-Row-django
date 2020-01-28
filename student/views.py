from django.shortcuts import render, redirect,HttpResponse
from django.shortcuts import get_object_or_404,Http404

#from rest_framework.response import Responsefrom django.contrib import messages
from django.views import View
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
from .token import activation_token

from .models import StudentProfile
from .forms import SearchStudentForm, StudentProfileForm

def home(request):
    std = StudentProfile.objects.all()
    context = {'students': std}
    return render(request,'home.html',context)


def student_list(request):
    std = StudentProfile.objects.all()
    context = {'students': std}
    return render(request, 'student/student_list.html', context)



def create_student(request):
    forms = StudentProfileForm()
    if request.method =='POST':
          forms =StudentProfileForm(request.POST)
          if forms.is_valid():
              instance = forms.save(commit=False)
              instance.is_active=False
              instance.save()
              site = get_current_site(request)
              mail_subject = "Confirmation message for blog"
              message = render_to_string('confirm_email.html', {
                  "user": instance,
                  'domain': site.domain,
                  'uid': instance.id,
                  'token': activation_token.make_token(instance)
              })
              to_email = forms.cleaned_data.get('email')
              to_list = [to_email]
              from_email = settings.EMAIL_HOST_USER
              send_mail(mail_subject, message, from_email, to_list, fail_silently=False)
              return HttpResponse("<h1>Thanks for your registration. A confirmation link was sent to your email</h1>")
    #forms = TeacherForm()
    context = {'forms': forms}
    return render(request, 'student/create_std.html', context)


def showall(request):
    ak = StudentProfile.objects.all()
    c = { 'a':ak}
    #messages.success(request, 'delete sucessfully')
    return render(request,'show.html',c)


def single(request,pid):
    a = StudentProfile.objects.get(email=pid)
    c = { 'a':a}
    #messages.success(request, 'delete sucessfully')
    return render(request,'show.html',c)



def mailToall(request):
    print("send all")
    ak = StudentProfile.objects.all()
    # print(ak)
    mail_list = []
    for v in ak:
        mail_list.append(v.email)
    print(mail_list)
    forms = StudentProfileForm()
    instance = forms.save(commit=False)
    instance.is_active = False
    # instance.save()
    site = get_current_site(request)
    # for mail in mail_list:
    mail_subject = "Info from the coaching Management"
    message = render_to_string('confirm_email.html', {
        "user": instance,
        'domain': site.domain,
        'uid': instance.id,
        'token': activation_token.make_token(instance)
    })
    # to_email = mail_list#forms.cleaned_data.get('email')
    # to_list = [to_email]
    from_email = settings.EMAIL_HOST_USER
    send_mail(mail_subject, message, from_email, mail_list, fail_silently=False)
    # print("sent to " + to_email)
    return HttpResponse("<h1>mail sent to all </h1>")


def edit_student(request, student_id):
    student_obj = StudentProfile.objects.get(id=student_id)
    forms = StudentProfileForm(instance=student_obj)
    if request.method == 'POST':
        forms = StudentProfileForm(request.POST, instance=student_obj)
        if forms.is_valid():
            forms.save()
            return redirect('student-list')
    context = {'forms': forms}
    return render(request, 'student/edit_std.html', context)





def delete_student(request, student_id):
    student_obj = StudentProfile.objects.get(id=student_id)
    student_obj.delete()
    return redirect('student-list')


def activate(request,uid ,token):
    try :
        user = get_object_or_404(pk = uid)
    except:
       raise Http404("No user Found")
    if user is not None and activation_token.check_token(user,token):
        user.is_active= True
        user.save()
        return HttpResponse("<h1> account is activated. </h1>")








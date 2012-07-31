import datetime, pymongo
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from guestbook.forms import MessageForm#,CaptchaTestForm
from django.template import RequestContext

def home(request):
    messages = pymongo.Connection().messages_db.messages
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            date = datetime.datetime.now()
            number = str(messages.find().count())
            messages.save({'number':number, 'date':date, 'name':
        'Noname' if cd.get('name') == '' else cd.get('name'),
                      'message':cd['message']})
            return HttpResponseRedirect('')
            #return render_to_response('form_template.html',{'messages':messages.find(), 'form':form},context_instance=RequestContext(request))
    else:
        form = MessageForm()
    for m in messages.find() :
            print m['number']
    return render_to_response('form_template.html', {'form': form,'messages':messages.find()}, context_instance=RequestContext(request))

def some_view(request):
    if request.POST:
        form = CaptchaTestForm(request.POST)

        # Validate the form: the captcha field will automatically
        # check the input
        if form.is_valid():
            human = True
    else:
        form = CaptchaTestForm()

    return render_to_response('template.html',locals())

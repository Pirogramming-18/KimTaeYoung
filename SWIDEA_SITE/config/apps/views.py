from django.shortcuts import render, redirect
from .models import Idea, devTool, ideaStar
from .forms import ideaForm, toolForm
# Create your views here.


def main_page(request):
  order = request.GET.get("order")

  stars = ideaStar.objects.all()

  if order:
    idea = Idea.objects.all().order_by(order)
  else:
    idea = Idea.objects.all()
  context = {"ideas" : idea, "stars" : stars}
  return render(request, "site/idea_list.html", context=context)

def create_idea(request):
  
  if request.method == 'POST':
    form = ideaForm(request.POST, request.FILES)

    ins = form.save() # form의 save는 저장된 instance를 return

    return redirect("apps:idea_detail", pk = ins.id)
  else:
    form = ideaForm()
    
  context = {"form" : form}
  return render(request, "site/create_idea.html", context=context)
  
  

def update_idea(request, pk):
  idea = Idea.objects.get(id=pk)
  if request.method == 'POST':
    form = ideaForm(request.POST, instance=idea)
    if form.is_valid():
      idea = form.save(commit = False)
      idea.image = request.FILES.get('image', None)
      idea.save()
      return redirect("apps:idea_detail", pk=idea.pk)
  else:
    form = ideaForm(instance=idea)
    context = {"form" : form, "idea" : idea}
  return render(request, "site/update_idea.html", context=context)

def delete_idea(request, pk):
  if request.method == "POST":
    detail = Idea.objects.get(id = pk)
    detail.delete()
    return redirect("apps:idea_list") 

def idea_detail(request, pk):
  detail = Idea.objects.get(id = pk)
  tool = detail.dev_tool
  context = {"detail" : detail}

  return render(request, "site/idea_detail.html", context=context)

def dev_delete(request, pk):
  if request.method == "POST":
    detail = devTool.objects.get(id = pk)
    detail.delete()
    return redirect("apps:dev_list") 

def dev_list(request):

  tools = devTool.objects.all()
  context = {"tools" : tools}
  
  return render(request, "site/dev_list.html", context=context)



def dev_detail(request, pk):
  detail = devTool.objects.get(id = pk)
  ideas = Idea.objects.all()
  all_idea = [] 
  for i in ideas:
    
    if str(i.dev_tool) == str(detail.name):
      all_idea.append(i)

  

  context = {"detail" : detail, "all_idea" : all_idea}

  return render(request, "site/dev_detail.html", context=context)


def dev_create(request):
  if request.method == 'POST':
    form = toolForm(request.POST, request.FILES)
    ins = form.save()
    return redirect("apps:dev_detail", pk = ins.id)
  
  return render(request, "site/dev_create.html")
  
def dev_update(request, pk):
  tool = devTool.objects.get(id=pk)
  if request.method == 'POST':
    form = toolForm(request.POST, request.FILES, instance=tool)
    ins = form.save()
    return redirect("apps:dev_detail", pk = ins.id)
  else:
    form = toolForm(instance=tool)
    context = {"form" : form, "tool" : tool}
  return render(request, "site/dev_update.html", context=context)
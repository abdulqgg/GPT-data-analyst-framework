from django.shortcuts import render, redirect
from django.http import FileResponse
from .forms import DocumentForm
from .your_script import your_function, python_visualise, explain_data

def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            api_key = str(request.POST.get('OPENAI_API_KEY'))
            user_query = str(request.POST.get('user_query'))
            
            # Trigger your script, assuming it writes the result to 'extracted-data.csv'
            your_function(document.txt_file.path, document.db_file.path, api_key, user_query)
            
            # Redirect to the download view to initiate the file download
            request.session['form_submitted'] = True
            return redirect('download_view')
    else:
        form = DocumentForm()

    form_submitted = request.session.get('form_submitted', False)
    
    return render(request, 'index.html', {'form': form, 'form_submitted': form_submitted})

def download_view(request):
    response = FileResponse(open('extracted-data.csv', 'rb'))
    response['Content-Disposition'] = 'attachment; filename="extracted-data.csv"'
    response['Content-Type'] = 'text/csv'
    return response

def python(request):
    if request.method == 'POST':
        charts_type = request.POST.get('visualization_type')
        if charts_type == 'chart':
            return python_visualise('chart')
        elif charts_type == 'graph':
            return python_visualise('graph')
        elif charts_type == 'table':
            return python_visualise('table')
    else:
        return render(request, 'index.html')

def explain(request):
    explaination = None

    if request.method == 'POST':
        user_query = str(request.POST.get('user_query'))
        explaination = explain_data(user_query)

    return render(request, 'index.html', {'explaination': explaination})
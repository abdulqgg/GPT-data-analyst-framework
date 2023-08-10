from django.shortcuts import render, redirect
from django.http import FileResponse
from .forms import DocumentForm
from .your_script import your_function

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
            return redirect('download_view')
    else:
        form = DocumentForm()
    
    return render(request, 'index.html', {'form': form})

def download_view(request):
    response = FileResponse(open('extracted-data.csv', 'rb'))
    response['Content-Disposition'] = 'attachment; filename="extracted-data.csv"'
    response['Content-Type'] = 'text/csv'
    return response



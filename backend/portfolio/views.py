from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer
from django.http import JsonResponse
import subprocess
import os

def run_box_ecm_script(request):
    # Make sure the script path is correct relative to your Django project root
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Run_Box_ECM.pyw')

    try:
        # Run the script and capture output
        result = subprocess.run(['python', script_path], capture_output=True, text=True, timeout=30)
        output = result.stdout
        error = result.stderr
    except subprocess.TimeoutExpired:
        return JsonResponse({'output': '', 'error': 'Script timed out'}, status=500)
    except Exception as e:
        return JsonResponse({'output': '', 'error': str(e)}, status=500)

    return JsonResponse({'output': output, 'error': error})

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-id')
    serializer_class = ProjectSerializer

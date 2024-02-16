from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import FileUploadParser
from django.forms.models import model_to_dict
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework import status
from .models import Bitcoin
from .serializers import FileSerializer, CsvSerializer
import csv


def home(request):
    if request.method == 'POST':
        csv_file_path = request.FILES.get('file')
       
        if csv_file_path:
            decoded_file = csv_file_path.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file)
            data = []
                
            for row in reader:

                data.append(Bitcoin(
                    date= row[0],
                    price= row[1],
                    open= row[2],
                    high= row[3],
                    low= row[4],
                    vol= row[5],
                    change= row[6]
                )) 
                
            created = Bitcoin.objects.bulk_create(data)
            res=[model_to_dict(x) for x in created]
            # return JsonResponse(data=res, safe = False, status=status.HTTP_201_CREATED)
            # return redirect( 'result', res = res)
            return render(request, 'result.html', {'data' : res , 'message': f"Added {len(res)} new data"})
        else:
            return JsonResponse(data={"message": "No file provided"},safe=False, status=status.HTTP_400_BAD_REQUEST)
    return render(request,'home.html')

def result(request,res=[]):
    res = request.GET.get('res', [])
    return render(request, 'result.html', {'data' : res , 'message': f"Added {len(res)} new data"})

class CsvReader(APIView):
    serializer_class = FileSerializer 
    queryset = Bitcoin
    
    def post(self, request, *args, **kwargs):
        csv_file_path = request.FILES.get('file')
       
        if csv_file_path:
            decoded_file = csv_file_path.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file)
            data = []
                
            for row in reader:
            
                data.append({
                    'date': row[0],
                    'price': row[1],
                    'open': row[2],
                    'high': row[3],
                    'low': row[4],
                    'vol': row[5],
                    'change': row[6]
                }) 
                
            serializer = CsvSerializer(data=data, many = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response({"message": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)
    
                
                
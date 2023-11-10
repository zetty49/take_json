from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from .models import Filters, FiltredData




@csrf_exempt
@require_POST
def add_data_to_db(request):
    filters_row = Filters.objects.first()
    f1 = filters_row.f1
    f2 = filters_row.f2
    f3 = filters_row.f3
    f4 = filters_row.f4
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            added_documents = 0
            for i in data:
                name = i.get('name')
                product_code = i.get('productCode')
                price = i.get('price')
                image = i.get('image')
                currency = i.get('currency')
                qty = i.get('qty')
                if f1 or f2 or f3 or f4 in product_code:
                        
                        FiltredData.objects.create(
                            name = name,
                            product_code = product_code,
                            price = price,
                            image = image,
                            currency = currency,
                            qty = qty,
                            
                        )
                        added_documents += 1

            return JsonResponse({'message': f'{added_documents} products added to the database'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
                
       
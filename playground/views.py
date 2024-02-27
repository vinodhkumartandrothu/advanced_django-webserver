import requests
import logging
from django.core.cache import cache
from django.shortcuts import render
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page



logger = logging.getLogger(__name__)


class HelloView(APIView):
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render(request, 'hello.html', {'name': 'Mosh'})



    




#first() method returns None. No need of try catch block
    #product = Product.objects.filter(pk=0).first()

    #queryset API - search
    #discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field = DecimalField())
    
    #collection = Collection()
    #collection.title = 'Video Games'
    #collection.featured_product = Product(pk=1)
    #collection.save()
    #collection.id


"""

    try:
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context = {'name':'Mosh'}
        )
        message.send(['john@moshbuy.com'])
       
    except BadHeaderError:
        pass
"""

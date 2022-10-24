
class SampleMiddleware:
  def __init__(self, get_response):
   self.get_response = get_response
   
  def __call__(self, request):
    
    print('Middleware execution before calling view')
    
    response = self.get_response(request)
    
    print('Middleware execution after calling view')
    
    return response
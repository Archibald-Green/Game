# from django.contrib.auth import authenticate, login

# def authLogin(get_response):

#     def middleware(request):
#         response = get_response(request)

#         return response

#     return middleware

# if b.first_page:
#         print ('_________________________-')
        
#         try: 
#             print ('zzzzzzzzzzzzzzzzzaaaaaaaaaaaaaaaa')
#             progress = models.BoolProgress.objects.get(book = b, user = request.user)
#         except models.BoolProgress.DoesNotExist:
#             print ('aaaaaaaaaaaaaaaa')
#             progress = models.BoolProgress.start_reading(user = request.user, book = b )
#             return render(request, 'main/book.html', context ={
#                 'book': b,
#             })
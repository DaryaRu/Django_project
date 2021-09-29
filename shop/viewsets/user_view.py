from shop.serializers.user_serializer import UserSerializer
from  rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework_jwt.settings import api_settings
from config.settings import SECRET_KEY
from django.contrib.auth.signals import user_logged_in
from rest_framework import status
from rest_framework.response import Response


class UserCreate(generics.CreateAPIView):
    queryset = get_user_model().objects
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
    
    def authenticate_user(request):

        try:
            username = request.data['username']
            password = request.data['password']

            user = get_user_model.objects.get(username=username, password=password)
            if user:
                try:
                    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                    payload = jwt_payload_handler(user)
                    token = jwt_encode_handler(payload, SECRET_KEY)
                    user_details = {}
                    # user_details['name'] = "%s %s" % (
                        # user.first_name, user.last_name)
                    user_details['token'] = token
                    user_logged_in.send(sender=user.__class__,
                                    request=request, user=user)
                    return Response(user_details, status=status.HTTP_200_OK)

                except Exception as e:
                    raise e
            else:
                res = {
                    'error': 'can not authenticate with the given credentials or the account has been deactivated'}
                return Response(res, status=status.HTTP_403_FORBIDDEN)
        except KeyError:
            res = {'error': 'please provide a username and a password'}
            return Response(res)    
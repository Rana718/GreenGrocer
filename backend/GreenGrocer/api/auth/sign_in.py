from .auth_utils import check_password, Response, status, get_collections

def signin_user(serializer):
    buyers_collection, sellers_collection = get_collections()

    user = buyers_collection.find_one({'username': serializer.validated_data['username']})
    if not user:
        user = sellers_collection.find_one({'username': serializer.validated_data['username']})

    if user:
        if check_password(serializer.validated_data['password'], user['password']):
            
            response_data = {
                'message': 'Login successful',
                'username': user['username'],
                'email': user['email'],
                'full_name': user['full_name'],
            }

            if 'rating' in user:
                response_data['rating'] = user['rating']

            return Response(response_data, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)

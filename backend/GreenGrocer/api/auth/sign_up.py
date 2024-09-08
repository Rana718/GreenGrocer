from .auth_utils import make_password, Response, status, get_collections


def sigup_user(serializer):
    buyers_collection, sellers_collection = get_collections()

    if buyers_collection.find_one({'username': serializer.validated_data['username']}) or sellers_collection.find_one({'username': serializer.validated_data['username']}):
        return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)

    hashed_password = make_password(serializer.validated_data['password'])

    user_data = {
        'full_name': serializer.validated_data['full_name'],
        'username': serializer.validated_data['username'],
        'email': serializer.validated_data['email'],
        'password': hashed_password,
    }

    if serializer.validated_data['user_type'] == 'buyer':
        buyers_collection.insert_one(user_data)
        return Response({'message': 'Buyer registered successfully'}, status=status.HTTP_201_CREATED)
    

    elif serializer.validated_data['user_type'] == 'seller':
        user_data['rating'] = 0.0
        sellers_collection.insert_one(user_data)
        return Response({'message': 'Seller registered successfully'}, status=status.HTTP_201_CREATED)
    
    return Response({'error': 'Invalid user type'}, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from controllers.models import Controller
from controllers.serializers import ControllerSerializer


@api_view(['GET', 'POST'])
def controller_list(request):
    """
    List all controllers, or create a new controller.
    """
    if request.method == 'GET':
        #snippets = Snippet.objects.all()
        controllers = Controller.all()
        serializer = ControllerSerializer(controllers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
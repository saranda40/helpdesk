from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticated
from icecream import ic

def generar_crud_api_view(Modelo, Serializer, id_key, name_key):

    @api_view(['GET', 'PATCH', 'POST', 'DELETE']) 
    @permission_classes([IsAuthenticated])
    def generic_view(request):
        
        item_id = request.query_params.get('id') 
        
        # --- GET (Obtener/Listar) ---
        if request.method == 'GET':
            if item_id is not None:
                try:
                    instance = Modelo.objects.get(pk=item_id) 
                    serializer = Serializer(instance) 
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except Modelo.DoesNotExist:
                    return Response(
                        {"detail": f"{name_key} con ID {item_id} no encontrado."},
                        status=status.HTTP_404_NOT_FOUND
                    )
                except Exception as e:
                     return Response({"detail": f"Error interno: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                queryset = Modelo.objects.all()
                serializer = Serializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

        # --- POST (Crear) ---
        if request.method == 'POST':
            data = request.data.copy()
            data['usr_crea'] = request.user.pk 
            
            serializer = Serializer(data=data)
            if serializer.is_valid():
                try:
                    instance = serializer.save()
                    return Response(Serializer(instance).data, status=status.HTTP_201_CREATED)
                except IntegrityError:
                    return Response({"error": f"Error de integridad: El registro de {name_key} ya existe o hay datos duplicados."}, status=status.HTTP_400_BAD_REQUEST)
                except Exception as e:
                    return Response({"error": f"Error durante la creación del {name_key}: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
        if request.methofd == 'DELETE':
            if not item_id:
                return Response({"error": f"Se requiere el 'id' del {name_key} para eliminar."}, status=status.HTTP_400_BAD_REQUEST)
            try:
                instance = Modelo.objects.get(pk=item_id)
                instance.delete()
                return Response({"detail": f"{name_key} con ID {item_id} eliminado correctamente."}, status=status.HTTP_200_OK)
            except Modelo.DoesNotExist:
                return Response(
                    {"detail": f"{name_key} con ID {item_id} no encontrado para eliminar."},
                    status=status.HTTP_404_NOT_FOUND
                )
            except Exception as e:
                return Response({"error": f"Error al eliminar el {name_key}: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if request.method == 'PUT':
            if not item_id:
                return Response({"error": f"Se requiere el 'id' del {name_key} para actualizar."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                instance = Modelo.objects.get(pk=item_id)
                
                data = request.data.copy() 
                data['usr_modifica'] = request.user.pk 

                serializer = Serializer(instance, data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            except Modelo.DoesNotExist:
                return Response(
                    {"detail": f"{name_key} con ID {item_id} no encontrado para actualizar."},
                    status=status.HTTP_404_NOT_FOUND
                )
            except Exception as e:
                return Response({"error": f"Error al actualizar el {name_key}: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # --- PATCH (Actualizar Parcial) ---
        if request.method == 'PATCH':
           
            if not item_id:
                return Response({"error": f"Se requiere el 'id' del {name_key} para actualizar."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                instance = Modelo.objects.get(pk=item_id)
                
                data = request.data.copy() 
                data['usr_modifica'] = request.user.pk 

                serializer = Serializer(instance, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            except Modelo.DoesNotExist:
                return Response(
                    {"detail": f"{name_key} con ID {item_id} no encontrado para actualizar."},
                    status=status.HTTP_404_NOT_FOUND
                )
            except Exception as e:
                return Response({"error": f"Error al actualizar el {name_key}: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"detail": "Método no permitido."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    return generic_view
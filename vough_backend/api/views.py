import api.exceptions as exceptions
from rest_framework import viewsets
from rest_framework.views import Response

from api import models, serializers
from api.integrations.github import GithubApi

from django.shortcuts import get_object_or_404

# TODOS:
# 1 - Buscar organização pelo login através da API do Github
# 2 - Armazenar os dados atualizados da organização no banco
# 3 - Retornar corretamente os dados da organização
# 4 - Retornar os dados de organizações ordenados pelo score na listagem da API


class OrganizationViewSet(viewsets.ModelViewSet):

    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer
    lookup_field = "login"

    def retrieve(self, request, login=None):
        try:
            organization = models.Organization.objects.get(login=login)
            serialize = serializers.OrganizationSerializer(organization)
            return Response(serialize.data)
        except models.Organization.DoesNotExist:
            try:
                organization = GithubApi().get_organization(login=login)
                serializer = serializers.OrganizationSerializer(data=organization)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=200)
                return Response(serializer.errors, status=400)
            except exceptions.InvalidTokenException as e:
                return Response(str(e), status=401)

from rest_framework import serializers
from DjangoRestAPI.Company.models import Company
from DjangoRestAPI.Dealer.serializers import DealerSerializer


class CompanySerializer(serializers.ModelSerializer):
    #url = serializers.HyperlinkedIdentityField()
    dealers = DealerSerializer(source='dealer_set', many=True)

    class Meta:
        fields = (
            'company_name',
            'working_area',
            'establish_year',
            'is_active',
            'location',
            'dealers',
        )
        model = Company


class CompanyUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = (
            'company_name',
            'working_area',
            'establish_year',
            'is_active',
            'location',
        )

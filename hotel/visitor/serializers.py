from rest_framework import serializers

from visitor.models import Details


class guestDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Details
        fields =['id', 'First_Name', 'Last_Name', 'Address', 'Adhar_id', 'Room_no', 'Time_in', 'Time_Out', 'Contact']
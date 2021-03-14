from rest_framework import serializers
from base.models import Manga

# class ResponsibleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Responsible
#         fields = '__all__'
#

class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = ['id', 'title', 'type_manga', "poster"]

    def to_representation(self, instance):
        """Convert `username` to lowercase."""
        ret = super().to_representation(instance)
        return ret


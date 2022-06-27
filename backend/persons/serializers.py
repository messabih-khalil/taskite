from rest_framework import serializers

from accounts.models import UserProfile

class UserInfoSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField('get_photo_url')
    class Meta:
        model = UserProfile
        fields = [
            "username", "nick_name" , "email" , "facebook","instagram" , "twitter" , "github","photo_url"
        ]
    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.profile_image.url
        return request.build_absolute_uri(photo_url)
class TeamFriendsSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField('get_photo_url')
    class Meta : 
        model = UserProfile
        fields = ["username" , "email" , "photo_url"]

    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.profile_image.url
        return request.build_absolute_uri(photo_url)
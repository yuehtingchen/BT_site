from curses.ascii import US
from rest_framework import serializers

from .models import Mentors
from school.serializers import HighSchoolSerializer, UniSerializer

class MentorsSerializer(serializers.HyperlinkedModelSerializer):
    high_school = HighSchoolSerializer(required = False)
    uni = UniSerializer(required = False)

    class Meta:
        model = Mentors
        fields = ('id','first_name', 'last_name', 'major','grad_year','email', 'linkedin','high_school', 'uni','intro','preferred_mentee_grade','other_preferences',"essay_editing")

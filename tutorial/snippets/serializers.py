from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

# Method to serialize snippet objects to a dictionary
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
	class Meta:
		model = Snippet
		fields = ('url', 'title', 'code', 'linenos', 'language', 'style', 'owner', 'highlight')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
	class Meta:
		model = User
		fields = ('url', 'username', 'snippets')
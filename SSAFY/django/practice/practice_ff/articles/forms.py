from django.forms.widgets import TextInput
from articles.models import Article
from django import forms

# class ArticleForm(forms.Form):
#     region_a = 'sl'
#     region_b = 'gj'
#     region_c = 'dj'
#     regions_choices = [
#         (region_a, '서울'),
#         (region_b, '광주'),
#         (region_c, '대전'),
#     ]
    
    
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     region = forms.ChoiceField(choices=regions_choices, widget=forms.Select())



class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget= forms.TextInput(
            attrs={
                'calss' : 'my-title',
                'placeholder' : 'Enter the title'
            }
        )
    )
    content = forms.CharField(
        label = '제목',
        widget= forms.Textarea(
            attrs={
                'calss' : 'my-content',
                'placeholder' : 'Enter the title',
                'rows' : 5,
                'cols' : 50
            }
        )
    )

    class Meta:
        model = Article
        fields = '__all__'

        # fiedls = ['title', 'content'] 이런식으로 할수도 있음
        # exclude = ('title',)  예외 처리 할때 사용
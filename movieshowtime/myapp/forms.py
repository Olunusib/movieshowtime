from django import forms


class MovieForm(forms.Form):
    actors = forms.CharField(label='choiceActors', max_length=100, required=False)
    genre = forms.MultipleChoiceField(label='choiceGenre',
                                      choices=[('Action', 'Action'), ('Drama', 'Drama'), ('Adventure', 'Adventure'),
                                               ('Fantasy', 'Fantasy'), ('Sci-Fi', 'Sci-Fi'), ('Comedy', 'Comedy')], required=False)
    movieNames = forms.CharField(label='MovieName', max_length=100, required=False)
    rating = forms.ChoiceField(label='choiceRating',
                               choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),
                                        ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], required=False)
    directors = forms.CharField(label='choiceDirectors', max_length=100, required=False)

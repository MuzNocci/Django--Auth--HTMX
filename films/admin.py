from django.contrib import admin
from films.models import FilmReview



@admin.register(FilmReview)
class ReviewAdmin(admin.ModelAdmin):

    list_display = [

        'title',
        'status',
        'rating',
        'created_at',

    ]

    list_filter = [

        'status',
        'author_id',
        
    ]

    search_fields = [

        'title',
        'body',

    ]
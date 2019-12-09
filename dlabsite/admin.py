from django.contrib import admin
from .models import (lab_member, publication,
    publication_link, job_listing, current_study,
    media_listing, data_listing, software_listing)

# admin for lab member model
class labmemberadmin(admin.ModelAdmin):
    ordering = ('last_name',)
    fieldsets = (
        ('Lab Member Data', {
            'fields': (
                'first_name',
                'last_name',
                'email',
                'phone',
                'title',
                'blurb',
                'alumni',
                'photo',
            )
        }),
    )
    search_fields = ('first_name','last_name','email','phone','title',)
    save_as = True

#inline model for publication link
class publicationlinkinline(admin.StackedInline):
    verbose_name = "Publication Link"
    model = publication_link

# admin for publication model
class publicationadmin(admin.ModelAdmin):
    ordering = ('-date',)
    fieldsets = (
        ('Publications', {
            'fields': (
                'title',
                'container',
                'date',
				'paper',
            )
        }),
    )
    inlines = (publicationlinkinline,)
    search_fields = ('title','container','date',)
    save_as = True

class joblistingadmin(admin.ModelAdmin):
    ordering = ('-post_date',)
    fieldsets = (
        ('Job Listing', {
            'fields': (
                'title',
                'jobid',
                'description',
            )
        }),
    )
    search_fields = ('title','jobid',)
    save_as = True

class currentstudyadmin(admin.ModelAdmin):
    ordering = ('title',)
    fieldsets = (
        ('Current Study', {
            'fields': (
                'title',
                'description',
                'link',
                'flier',
            )
        }),
    )
    search_fields = ('title',)
    save_as = True

class medialistingadmin(admin.ModelAdmin):
    ordering = ('-date',)
    fieldsets = (
        ('media Listing', {
            'fields': (
                'title',
                'description',
                'link',
                'image',
                'date',
            )
        }),
    )
    search_fields = ('title', 'date',)
    save_as = True

class datalistingadmin(admin.ModelAdmin):
    ordering = ('title',)
    fieldsets = (
        ('Data Listing', {
            'fields': (
                'title',
                'description',
                'link',
                'image',
            )
        }),
    )
    search_fields = ('title',)
    save_as = True

class softwarelistingadmin(admin.ModelAdmin):
    ordering = ('title',)
    fieldsets = (
        ('Software Listing', {
            'fields': (
                'title',
                'description',
                'link',
                'image',
            )
        }),
    )
    search_fields = ('title',)
    save_as = True

# dlabsite models
admin.site.register(lab_member, labmemberadmin)
admin.site.register(publication, publicationadmin)
admin.site.register(job_listing, joblistingadmin)
admin.site.register(current_study, currentstudyadmin)
admin.site.register(media_listing, medialistingadmin)
admin.site.register(data_listing, datalistingadmin)
admin.site.register(software_listing, softwarelistingadmin)

# customize admin site names
admin.site.site_title = 'Admin'
admin.site.site_header = 'Dosenbach Lab Admin'
admin.site.index_title = 'Home'

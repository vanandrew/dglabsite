from django.contrib import admin
from .models import (lab_member, research, publication,
    research_image, publication_link, job_listing)

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

#inline model for research image
class researchimginline(admin.StackedInline):
    verbose_name = "Research Image"
    model = research_image

#inline model for publication link
class publicationlinkinline(admin.StackedInline):
    verbose_name = "Publication Link"
    model = publication_link

# admin for research model
class researchadmin(admin.ModelAdmin):
    ordering = ('title',)
    fieldsets = (
        ('Research Summary', {
            'fields': (
                'title',
                'description',
            )
        }),
    )
    inlines = (researchimginline,)
    search_fields = ('title',)
    save_as = True

# admin for publication model
class publicationadmin(admin.ModelAdmin):
    ordering = ('-date',)
    fieldsets = (
        ('Publications', {
            'fields': (
                'title',
                'container',
                'date',
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

# dlabsite models
admin.site.register(lab_member, labmemberadmin)
admin.site.register(research, researchadmin)
admin.site.register(publication, publicationadmin)
admin.site.register(job_listing, joblistingadmin)

# customize admin site names
admin.site.site_title = 'Admin'
admin.site.site_header = 'Dosenbach Lab Admin'
admin.site.index_title = 'Home'

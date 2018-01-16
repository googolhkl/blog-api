from django.contrib import admin
from .models import PrivateInformation, Skill, Education, Experience, Project, SelfIntroduction

@admin.register(PrivateInformation)
class PrivateInformationAdmin(admin.ModelAdmin):
    list_display = (['name'])

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('host',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(SelfIntroduction)
class SelfIntroductionAdmin(admin.ModelAdmin):
    list_display = ('subject',)

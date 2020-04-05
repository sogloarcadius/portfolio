from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    name = 'apps.projects'
    label = "projects"
    verbose_name = "Projects"
    


default_app_config = "apps.projects.ProjectsConfig"
from django.contrib import admin
from .models import Post
from .models import CV
from .models import WorkExperience
from .models import Education
from .models import Activity

# Register your models here.
admin.site.register(Post)
admin.site.register(CV)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Activity)
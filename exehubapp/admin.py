from django.contrib import admin

from .models import Posts
from .models import UniGroups
from .models import Users
from .models import Attendees
from .models import Members

# Register models with admin.
admin.site.register(Posts)
admin.site.register(UniGroups)
admin.site.register(Users)
admin.site.register(Attendees)
admin.site.register(Members)


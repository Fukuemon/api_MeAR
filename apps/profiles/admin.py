from django.contrib import admin
# Django adminとauth.adminから必要なモジュールをインポート
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# 多言語化をサポートするgettextをインポート
from django.utils.translation import gettext as _
# このアプリケーションのモデルをインポート
from . import models

# Register your models here.
admin.site.register(models.Profile)
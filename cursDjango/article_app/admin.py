from django.contrib import admin
from .models import Article
from django.core import serializers
from django.http import HttpResponse
import pandas as pd


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    actions = ['export_as_json', 'export_as_xlsx']

    @admin.action(description='Export as json')
    def export_as_json(self, request, queryset):
        response = HttpResponse(content_type="application/json")
        response['Content-Disposition'] = 'attachment; filename="articles.json"'
        serializers.serialize("json", queryset, stream=response)
        return response

    @admin.action(description='Export as XLSX')
    def export_as_xlsx(self, request, queryset):
        # Преобразование данных в DataFrame
        data = queryset.values()  # Получение всех объектов queryset как словаря
        df = pd.DataFrame(list(data))

        for column in df.columns:
            if pd.api.types.is_datetime64_any_dtype(df[column]):
                df[column] = df[column].dt.tz_localize(None)

        # Указание MIME-типа и имени файла
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="articles.xlsx"'

        # Сохранение DataFrame в Excel файл в объекте ответа
        with pd.ExcelWriter(response, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Articles')

        return response

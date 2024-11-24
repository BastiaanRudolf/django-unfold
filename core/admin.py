import json
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from unfold.admin import ModelAdmin
from unfold.views import UnfoldModelAdminViewMixin

from polls.models import Question, Choice


@admin.register(Question)
class QuestionAdminClass(ModelAdmin):
    pass

@admin.register(Choice)
class ChoiceAdminClass(ModelAdmin):
    pass


# Custom dasboard view
admin.site.index_title = 'Dashboard'

class DashboardView(UnfoldModelAdminViewMixin, TemplateView):
    title = "Dashboard"
    template_name = "admin/index.html"
    permission_required = ()


class DashboardAdmin(ModelAdmin):
    def get_urls(self):
        return super().get_urls() + [
            path(
                "index", 
                DashboardView.as_view(model_admin=self),
                name="index"
            ),
        ]


def dashboard_callback(request, context):
    """
    Callback to prepare custom variables for index template which is used as dashboard
    template. It can be overridden in application by creating custom admin/index.html.
    """
    # Send data to dashboard
    context.update(
        {
        "kpis": [
            {
                "title": "Total Active Users (Last 7 days)",
                "metric": 10,
            },
            {
                "title": "Number of Polls (Last 7 days)",
                "metric": 7,
            },
            {
                "title": "Total Active Organisations",
                "metric": 18,
            },
        ],

        "dauChartData": json.dumps({
            'datasets': [
                {'data': [0,1,3,2,5,8,7],
                'borderColor': 'rgb(147 51 234)'
                }
            ],
            'labels': [
                '2024-11-18',
                '2024-11-19',
                '2024-11-20',
                '2024-11-21',
                '2024-11-22',
                '2024-11-23',
                '2024-11-24'
            ]
        }),

        "dpsChartData": json.dumps({
            'datasets': [
                {'data': [7,15,12,23,5,10,18],
                'borderColor': 'rgb(147 51 234)'
                }
            ],
            'labels': [
                '2024-11-18',
                '2024-11-19',
                '2024-11-20',
                '2024-11-21',
                '2024-11-22',
                '2024-11-23',
                '2024-11-24'
            ]
        }),

        "table": {
            "headers": ["Awesome column", "This one too!"],
            "rows": [
                ["a", "b"],
                ["c", "d"],
                ["e", "f"],
            ]
        },

        }
    )
    return context

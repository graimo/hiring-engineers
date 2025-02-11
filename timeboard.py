
from datadog import initialize, api
#import os


options = {
            #'api_key': os.environ["DD_API_KEY"],
             #   'app_key': os.environ["DD_APP_KEY"]
             'api_key': '<DATADOG_API_KEY>',
             'app_key': '<DATADOG_APPLICATION_KEY>'
                }

initialize(**options)

title = 'Test Dashboard'
widgets = [
        {'definition': {
            'type': 'timeseries',
            'requests': [
                {'q': 'avg:my_metric{host:GiuseppeInterview}'}],
            'title': 'my_metric'
            }
            },
        {'definition': {
            'type': 'timeseries',
            'requests': [
                {'q': "anomalies(avg:mongodb.mem.bits{host:GiuseppeInterview}, 'basic', 2)"}],
            'title': 'MongoDB in-memory storage engine'
            }
            },
        {'definition': {
            'type': 'timeseries',
            'requests': [
                {'q': 'avg:my_metric{host:GiuseppeInterview}.rollup(sum, 3600)'}],
            'title': 'my_metric rollup 1h'
            }
            }
        ]

layout_type = 'ordered'
description = '2nd step of the Interview assignment'
is_read_only = True
notify_list = ['giuseppe.raimo95@gmail.com']
template_variables = [{
    'name': 'Test',
    'prefix': 'host',
    'default': 'my-host'
    }]

api.Dashboard.create(title=title,
        widgets=widgets,
        layout_type=layout_type,
        description=description,
        is_read_only=is_read_only,
        notify_list=notify_list,
        template_variables=template_variables)

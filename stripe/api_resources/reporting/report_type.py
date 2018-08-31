from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource


class ReportType(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = 'reporting.report_type'

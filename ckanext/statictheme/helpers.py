import ckan.lib.helpers as h
import ckan.plugins.toolkit as toolkit
import ckan.plugins as plugins
import datetime
from ckan import model
from sqlalchemy import func

from collections import Counter
import logging
log = logging.getLogger(__name__)


def repositories_dataset_present_count():
    """Number of repositories in CKAN organizations &
    Number of datasets in the repositories list. """
    each_repo_count = []

    list_org = toolkit.get_action('organization_list')(
        data_dict={'type': 'repository', 'sort': 'package_count desc', 'all_fields': True})

    org = list_org
    count_to_display_repo = len(list_org)

    for package_count in list_org:
        each_repo_count.append(package_count['package_count'])

    count_to_display_dataset = sum(each_repo_count)

    return org, count_to_display_repo, count_to_display_dataset

def get_measurement_count(name,search_facets):
    """Number of datasets with measurement_technique_proxy field present."""

    return 'Nothing o Return'


def get_recent_datasets_by_org():

    one_month_ago = datetime.datetime.utcnow() - datetime.timedelta(days=90)

    query = (
        model.Session.query(model.Package.owner_org, func.count(model.Package.id))
        .filter(model.Package.metadata_created >= one_month_ago)
        .filter(model.Package.state == 'active')
        .filter(model.Package.private == False)
        .group_by(model.Package.owner_org)
    )

    return {org_id: count for org_id, count in query}
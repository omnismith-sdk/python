# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from omnismith_sdk.api.access_tokens_api import AccessTokensApi
    from omnismith_sdk.api.attributes_api import AttributesApi
    from omnismith_sdk.api.auth_api import AuthApi
    from omnismith_sdk.api.automation_automations_api import AutomationAutomationsApi
    from omnismith_sdk.api.automation_notification_channels_api import AutomationNotificationChannelsApi
    from omnismith_sdk.api.automation_push_devices_api import AutomationPushDevicesApi
    from omnismith_sdk.api.billing_api import BillingApi
    from omnismith_sdk.api.dashboard_blocks_api import DashboardBlocksApi
    from omnismith_sdk.api.dashboards_api import DashboardsApi
    from omnismith_sdk.api.entity_api import EntityApi
    from omnismith_sdk.api.feedback_api import FeedbackApi
    from omnismith_sdk.api.file_attachment_api import FileAttachmentApi
    from omnismith_sdk.api.marketplace_api import MarketplaceApi
    from omnismith_sdk.api.projects_api import ProjectsApi
    from omnismith_sdk.api.roles_api import RolesApi
    from omnismith_sdk.api.saved_queries_api import SavedQueriesApi
    from omnismith_sdk.api.schema_api import SchemaApi
    from omnismith_sdk.api.templates_api import TemplatesApi
    from omnismith_sdk.api.user_api import UserApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from omnismith_sdk.api.access_tokens_api import AccessTokensApi
from omnismith_sdk.api.attributes_api import AttributesApi
from omnismith_sdk.api.auth_api import AuthApi
from omnismith_sdk.api.automation_automations_api import AutomationAutomationsApi
from omnismith_sdk.api.automation_notification_channels_api import AutomationNotificationChannelsApi
from omnismith_sdk.api.automation_push_devices_api import AutomationPushDevicesApi
from omnismith_sdk.api.billing_api import BillingApi
from omnismith_sdk.api.dashboard_blocks_api import DashboardBlocksApi
from omnismith_sdk.api.dashboards_api import DashboardsApi
from omnismith_sdk.api.entity_api import EntityApi
from omnismith_sdk.api.feedback_api import FeedbackApi
from omnismith_sdk.api.file_attachment_api import FileAttachmentApi
from omnismith_sdk.api.marketplace_api import MarketplaceApi
from omnismith_sdk.api.projects_api import ProjectsApi
from omnismith_sdk.api.roles_api import RolesApi
from omnismith_sdk.api.saved_queries_api import SavedQueriesApi
from omnismith_sdk.api.schema_api import SchemaApi
from omnismith_sdk.api.templates_api import TemplatesApi
from omnismith_sdk.api.user_api import UserApi

""",
            name=__name__,
            doc=__doc__,
        )
    )

# Omnismith Python SDK

[![npm version](https://img.shields.io/npm/v/@omnismith-sdk%2Ftypescript)](https://www.npmjs.com/package/@omnismith-sdk/typescript)
[![PyPI version](https://img.shields.io/pypi/v/omnismith-sdk)](https://pypi.org/project/omnismith-sdk/)
[![Packagist version](https://img.shields.io/packagist/v/omnismith-sdk/php)](https://packagist.org/packages/omnismith-sdk/php)
[![Go Report Card](https://goreportcard.com/badge/github.com/omnismith-sdk/go)](https://goreportcard.com/report/github.com/omnismith-sdk/go)

The Omnismith Python SDK is generated from the central OpenAPI contract for the [Omnismith platform](https://omnismith.io), a flexible data management system built around templates, entities, and attribute-driven schemas. Use it to automate workflows against the Omnismith API and pair it with the web app at [app.omnismith.io](https://app.omnismith.io).

## Quick Start

```python
import os

from omnismith_sdk import ApiClient, Configuration
from omnismith_sdk.api.entity_api import EntityApi
from omnismith_sdk.api.templates_api import TemplatesApi
from omnismith_sdk.models.create_entity_request import CreateEntityRequest

configuration = Configuration(
    host="https://api.omnismith.io/v1",
    access_token=os.environ["OMNISMITH_ACCESS_TOKEN"],
)

with ApiClient(configuration) as api_client:
    templates_api = TemplatesApi(api_client)
    entity_api = EntityApi(api_client)

    template_id = "your-template-id"
    template = templates_api.get_template(template_id)

    entity = entity_api.create_entity(
        create_entity_request=CreateEntityRequest.from_dict(
            {
                "template_id": template.id,
                "attribute_values": [
                    {
                        "attribute_id": template.attribute_ids[0],
                        "value": "SKU-1001",
                    }
                ],
            }
        )
    )

    print(template.name, entity.id)
```

Set `OMNISMITH_ACCESS_TOKEN` to an access token created in Omnismith before running the snippet.
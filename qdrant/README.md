# Qdrant

<img width="1139" alt="Qdrant Datadog Dashboard" src="https://raw.githubusercontent.com/DataDog/integrations-extras/master/qdrant/images/qdrant_dashboard.png">

## Overview

[Qdrant][1] is a high-performance vector search engine/database. Use the Datadog integration to get metrics in real-time to monitor your Qdrant deployment.

For a full list of supported metrics, see the **Metrics** section below.

## Setup

The Qdrant check is not included in the [Datadog Agent][2] package, so you need to install it.

### Installation

For Agent v7.21+ / v6.21+, follow the instructions below to install the Qdrant check on your host. See [Use Community Integrations][3] to install with the Docker Agent or earlier versions of the Agent.

1. Run the following command to install the Agent integration:

   ```shell
   datadog-agent integration install -t qdrant==<INTEGRATION_VERSION>
   ```

2. Configure your integration similar to core [integrations][4].

### Configuration

1. Edit the `qdrant.d/conf.yaml` file in the `conf.d/` folder at the root of your [Agent's configuration directory][7] to start collecting your Qdrant [metrics](#metrics).

2. [Restart the Agent][9]

## Validation

Run the [Agent's status subcommand][10] and look for `qdrant` under the Checks section.

## Data Collected

### Metrics

See [metadata.csv][11] for a list of metrics provided by this check.

### Events

The Qdrant check does not include any events.

### Service Checks

See [service_checks.json][13] for a list of service checks provided by this integration.

## Troubleshooting

Need help? Contact [Datadog support][12].

[1]: https://qdrant.tech/
[2]: https://app.datadoghq.com/account/settings/agent/latest
[3]: https://docs.datadoghq.com/agent/guide/use-community-integrations/
[4]: https://docs.datadoghq.com/getting_started/integrations/
[7]: https://docs.datadoghq.com/agent/guide/agent-configuration-files/#agent-configuration-directory
[9]: https://docs.datadoghq.com/agent/guide/agent-commands/#start-stop-and-restart-the-agent
[10]: https://docs.datadoghq.com/agent/guide/agent-commands/#service-status
[11]: https://github.com/DataDog/integrations-extras/blob/master/qdrant/metadata.csv
[12]: http://docs.datadoghq.com/help
[13]: https://github.com/DataDog/integrations-extras/blob/master/qdrant/assets/service_checks.json

import os
import datetime
import asyncio

from azure.ai.metricsadvisor import (
    MetricsAdvisorKeyCredential,
    MetricsAdvisorAdministrationClient,
)

from azure.ai.metricsadvisor.models import (
    SqlServerDataFeedSource,
    DataFeedSchema,
    DataFeedMetric,
    DataFeedDimension,
    DataFeedGranularity,
    DataFeedGranularityType,
    DataFeedIngestionSettings,
    DataFeed,
)

async def task():
    endpoint = os.getenv("ENDPOINT")
    subscriptionKey = os.getenv("SUBSCRIPTION_KEY")
    apiKey = os.getenv("API_KEY")

    credential = MetricsAdvisorKeyCredential(subscriptionKey, apiKey)
    adminClient = MetricsAdvisorAdministrationClient(endpoint, credential)

    sqlServerConnectionString = os.getenv("SQL_SERVER_CONNECTION_STRING")
    sqlServerQuery = "SELECT @IntervalStart as timestamp," \
        + " region, category, revenue, cost FROM MASampleRevenueCost " \
        + "WHERE timestamp >= @IntervalStart and timestamp < @IntervalEnd"

    # set Datafeed
    name = "Sample data feed"
    source = SqlServerDataFeedSource(sqlServerConnectionString, sqlServerQuery)
    granularity = DataFeedGranularity(DataFeedGranularityType.Daily)

    schema = DataFeedSchema()
    schema.MetricColumns.Add(DataFeedMetric("revenue"))
    schema.DimensionColumns.Add(DataFeedDimension("category"))
    schema.DimensionColumns.Add(DataFeedDimension("city"))
    schema.MetricColumns.Add(DataFeedMetric("cost"))

    ingestionSettings = DataFeedIngestionSettings(
        datetime.strptime("2020-01-01T00:00:00Z"))

    dataFeed = DataFeed(name, source, granularity, schema, ingestionSettings)

    response = await adminClient.CreateDataFeedAsync(dataFeed)
    createdDataFeed = response.Value

    print(f"Data feed ID: {createdDataFeed.Id}")
    print(f"Data feed status: {createdDataFeed.Status.Value}")
    print(f"Data feed created time: {createdDataFeed.CreatedOn.Value}")

    print(f"Data feed administrators:")

    for admin in createdDataFeed.Administrators:
        print(f" - {admin}")

    print(f"Metric IDs:")

    for metric in createdDataFeed.Schema.MetricColumns:
        print(f" - {metric.Name}: {metric.Id}")

    print(f"Dimensions:")

    for dimension in createdDataFeed.Schema.DimensionColumns:
        print(f"- {dimension.Name}")

asyncio.run(task())

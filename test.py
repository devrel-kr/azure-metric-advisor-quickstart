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
    DataFeed
)

# TODO: async
endpoint ="ENDPOINT"
subscriptionKey = "SUBSCRIPTION_KEY"
apiKey = "API_KEY"

sqlServerConnectionString = ""
credential = MetricsAdvisorKeyCredential(subscriptionKey, apiKey)
adminClient = MetricsAdvisorAdministrationClient(endpoint, credential)
 

# Security
sqlServerConnectionString = ""
sqlServerQuery = "SELECT @IntervalStart as timestamp, region, category, revenue, cost FROM MASampleRevenueCost WHERE timestamp >= @IntervalStart and timestamp < @IntervalEnd"

#dataFeed = DataFeed("Change Me!!")
#dataFeed.Name = "Change Me!!"

Source = SqlServerDataFeedSource(sqlServerConnectionString, sqlServerQuery)
Granularity = DataFeedGranularity(DataFeedGranularityType.Daily)

Schema = DataFeedSchema()
Schema.MetricColumns.Add(DataFeedMetric("revenue"))
Schema.DimensionColumns.Add(DataFeedDimension("category"))
Schema.DimensionColumns.Add(DataFeedDimension("city"))
IngestionSettings = DataFeedIngestionSettings(datetime.strptime("2020-01-01T00:00:00Z"))
Schema.MetricColumns.Add(DataFeedMetric("cost"))

dataFeed = DataFeed("Change Me!!", Source, Granularity, Schema, IngestionSettings)


# TODO
# Response<DataFeed> response = await adminClient.CreateDataFeedAsync(dataFeed);
# DataFeed createdDataFeed = response.Value;

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

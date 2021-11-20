import os

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
)

# TODO: async
# TODO: where to get
endpoint = os.getenv("ENDPOINT")
subscriptionKey = os.getenv("SUBSCRIPTION_KEY")
apiKey = os.getenv("API_KEY")

credential = MetricsAdvisorKeyCredential(subscriptionKey, apiKey)
adminClient = MetricsAdvisorAdministrationClient(endpoint, credential)

# Security
sqlServerConnectionString = ""
sqlServerQuery = "SELECT @IntervalStart as timestamp, region, category, revenue, cost FROM MASampleRevenueCost WHERE timestamp >= @IntervalStart and timestamp < @IntervalEnd"

# TODO: dataFeed
dataFeed = DataFeed
dataFeed.Name = "Change Me!!"

dataFeed.DataSource = SqlServerDataFeedSource(sqlServerConnectionString, sqlServerQuery)
dataFeed.Granularity = DataFeedGranularity(DataFeedGranularityType.Daily)

dataFeed.Schema = DataFeedSchema()
dataFeed.Schema.MetricColumns.Add(DataFeedMetric("cost"))
dataFeed.Schema.MetricColumns.Add(DataFeedMetric("revenue"))
dataFeed.Schema.DimensionColumns.Add(DataFeedDimension("category"))
dataFeed.Schema.DimensionColumns.Add(DataFeedDimension("city"))

# TODO: DateTimeOffset
dataFeed.IngestionSettings = DataFeedIngestionSettings(DateTimeOffset.Parse("2020-01-01T00:00:00Z"))

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

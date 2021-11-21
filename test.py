import os
import datetime

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
)

endpoint = os.getenv("ENDPOINT")
subscriptionKey = os.getenv("SUBSCRIPTION_KEY")
apiKey = os.getenv("API_KEY")

credential = MetricsAdvisorKeyCredential(subscriptionKey, apiKey)
adminClient = MetricsAdvisorAdministrationClient(endpoint, credential)

sqlServerConnectionString = os.getenv("SQL_SERVER_CONNECTION_STRING")
sqlServerQuery = "SELECT @IntervalStart as timestamp, region, category, revenue, cost FROM MASampleRevenueCost WHERE timestamp >= @IntervalStart and timestamp < @IntervalEnd"

# set Datafeed
name = "<change name>"
source = SqlServerDataFeedSource(connection_string=sqlServerConnectionString, query=sqlServerQuery)
granularity = DataFeedGranularity(DataFeedGranularityType.Daily)

schema = DataFeedSchema(
    metrics=[
        DataFeedMetric(name="cost", display_name="Cost"),
        DataFeedMetric(name="revenue", display_name="Revenue")
    ],
    dimensions=[
        DataFeedDimension(name="category", display_name="Category"),
        DataFeedDimension(name="city", display_name="City")
    ],
)

ingestionSettings = datetime.datetime(2019, 10, 1)

dataFeed = adminClient.create_data_feed(name, source, granularity, schema, ingestionSettings)

# print data inside of the dataFeed
print(f"Data feed ID: {dataFeed.id}")
print(f"Data feed status: {dataFeed.status}")
print(f"Data feed created time: {dataFeed.created_time}")

print(f"Data feed administrators:")

for admin in dataFeed.admins:
    print(f" - {admin}")

print(f"Metric IDs:")

for metric in dataFeed.schema.metrics:
    print(f" - {metric.name}: {metric.id}")

print(f"Dimensions:")

for dimension in dataFeed.schema.dimensions:
    print(f"- {dimension.name}")

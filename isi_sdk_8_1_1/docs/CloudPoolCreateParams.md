# CloudPoolCreateParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **list[str]** | A list of valid names for the accounts in this pool.  There is currently only one account allowed per pool. | 
**birth_cluster_id** | **str** | The guid of the cluster where this pool was created | [optional] 
**description** | **str** | A brief description of this pool | [optional] 
**name** | **str** | A unique name for this pool | 
**vendor** | **str** | A string identifier of the cloud services vendor | [optional] 
**type** | **str** | The type of cloud protocol required.  E.g., \&quot;isilon\&quot; for EMC Isilon, \&quot;ecs\&quot; for EMC ECS Appliance, \&quot;virtustream\&quot; for Virtustream Storage Cloud, \&quot;azure\&quot; for Microsoft Azure, \&quot;s3\&quot; for Amazon S3 and \&quot;google\&quot; for Google Cloud Platform | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



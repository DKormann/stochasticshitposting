#%%

from google.cloud import aiplatform
from vertexai import preview
import vertexai
aiplatform.init(
    # your Google Cloud Project ID or number
    # environment default used is not set
    project='764195765676408832',

    # the Vertex AI region you will use
    # defaults to us-central1
    location='us-east4',

    # Google Cloud Storage bucket in same region as location
    # used to stage artifacts
    staging_bucket='gs://video-bucket-blisstagram',

    # custom google.auth.credentials.Credentials
    # environment default credentials used if not set
    # credentials=my_credentials,

    # customer managed encryption key resource name
    # will be applied to all Vertex AI resources if set
    # encryption_spec_key_name=my_encryption_key_name,

    # the name of the experiment to use to track
    # logged metrics and parameters
    # experiment='my-experiment',

    # description of the experiment above
    # experiment_description='my experiment description'
)
# %%
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START aiplatform_predict_custom_trained_model_sample]
from typing import Dict, List, Union

from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value


def predict_custom_trained_model_sample(
    project: str,
    endpoint_id: str,
    instances: Union[Dict, List[Dict]],
    location: str = "us-east4",
    api_endpoint: str = "us-east4-aiplatform.googleapis.com",
):
    """
    `instances` can be either single instance of type dict or a list
    of instances.
    """
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)
    # The format of each instance should conform to the deployed model's prediction input schema.
    instances = instances if isinstance(instances, list) else [instances]
    instances = [
        json_format.ParseDict(instance_dict, Value()) for instance_dict in instances
    ]
    parameters_dict = {}
    parameters = json_format.ParseDict(parameters_dict, Value())
    endpoint = client.endpoint_path(
        project=project, location=location, endpoint=endpoint_id
    )
    response = client.predict(
        endpoint=endpoint, instances=instances, parameters=parameters
    )
    print("response")
    print(" deployed_model_id:", response.deployed_model_id)
    # The predictions are a google.protobuf.Value representation of the model's predictions.
    predictions = response.predictions
    for prediction in predictions:
        print(" prediction:", dict(prediction))


# [END aiplatform_predict_custom_trained_model_sample]
# %%
predict_custom_trained_model_sample(
    project="682865449797",
    endpoint_id="764195765676408832",
    location="us-east4",
    instances={ "prompt": "butterfly"}
)
# %%

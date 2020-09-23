# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from .annotation_spec import AnnotationSpec
from .io import (
    GcsSource,
    GcsDestination,
    BigQuerySource,
    BigQueryDestination,
    ContainerRegistryDestination,
)
from .dataset import (
    Dataset,
    ImportDataConfig,
    ExportDataConfig,
)
from .manual_batch_tuning_parameters import ManualBatchTuningParameters
from .completion_stats import CompletionStats
from .model_evaluation_slice import ModelEvaluationSlice
from .machine_resources import (
    MachineSpec,
    DedicatedResources,
    AutomaticResources,
    BatchDedicatedResources,
    ResourcesConsumed,
)
from .deployed_model_ref import DeployedModelRef
from .env_var import EnvVar
from .explanation_metadata import ExplanationMetadata
from .explanation import (
    Explanation,
    ModelExplanation,
    Attribution,
    ExplanationSpec,
    ExplanationParameters,
    SampledShapleyAttribution,
)
from .model import (
    Model,
    PredictSchemata,
    ModelContainerSpec,
    Port,
)
from .training_pipeline import (
    TrainingPipeline,
    InputDataConfig,
    FractionSplit,
    FilterSplit,
    PredefinedSplit,
    TimestampSplit,
)
from .model_evaluation import ModelEvaluation
from .batch_prediction_job import BatchPredictionJob
from .custom_job import (
    CustomJob,
    CustomJobSpec,
    WorkerPoolSpec,
    ContainerSpec,
    PythonPackageSpec,
    Scheduling,
)
from .specialist_pool import SpecialistPool
from .data_labeling_job import (
    DataLabelingJob,
    ActiveLearningConfig,
    SampleConfig,
    TrainingConfig,
)
from .study import (
    Trial,
    StudySpec,
    Measurement,
)
from .hyperparameter_tuning_job import HyperparameterTuningJob
from .job_service import (
    CreateCustomJobRequest,
    GetCustomJobRequest,
    ListCustomJobsRequest,
    ListCustomJobsResponse,
    DeleteCustomJobRequest,
    CancelCustomJobRequest,
    CreateDataLabelingJobRequest,
    GetDataLabelingJobRequest,
    ListDataLabelingJobsRequest,
    ListDataLabelingJobsResponse,
    DeleteDataLabelingJobRequest,
    CancelDataLabelingJobRequest,
    CreateHyperparameterTuningJobRequest,
    GetHyperparameterTuningJobRequest,
    ListHyperparameterTuningJobsRequest,
    ListHyperparameterTuningJobsResponse,
    DeleteHyperparameterTuningJobRequest,
    CancelHyperparameterTuningJobRequest,
    CreateBatchPredictionJobRequest,
    GetBatchPredictionJobRequest,
    ListBatchPredictionJobsRequest,
    ListBatchPredictionJobsResponse,
    DeleteBatchPredictionJobRequest,
    CancelBatchPredictionJobRequest,
)
from .user_action_reference import UserActionReference
from .annotation import Annotation
from .operation import (
    GenericOperationMetadata,
    DeleteOperationMetadata,
)
from .endpoint import (
    Endpoint,
    DeployedModel,
)
from .prediction_service import (
    PredictRequest,
    PredictResponse,
    ExplainRequest,
    ExplainResponse,
)
from .endpoint_service import (
    CreateEndpointRequest,
    CreateEndpointOperationMetadata,
    GetEndpointRequest,
    ListEndpointsRequest,
    ListEndpointsResponse,
    UpdateEndpointRequest,
    DeleteEndpointRequest,
    DeployModelRequest,
    DeployModelResponse,
    DeployModelOperationMetadata,
    UndeployModelRequest,
    UndeployModelResponse,
    UndeployModelOperationMetadata,
)
from .pipeline_service import (
    CreateTrainingPipelineRequest,
    GetTrainingPipelineRequest,
    ListTrainingPipelinesRequest,
    ListTrainingPipelinesResponse,
    DeleteTrainingPipelineRequest,
    CancelTrainingPipelineRequest,
)
from .specialist_pool_service import (
    CreateSpecialistPoolRequest,
    CreateSpecialistPoolOperationMetadata,
    GetSpecialistPoolRequest,
    ListSpecialistPoolsRequest,
    ListSpecialistPoolsResponse,
    DeleteSpecialistPoolRequest,
    UpdateSpecialistPoolRequest,
    UpdateSpecialistPoolOperationMetadata,
)
from .model_service import (
    UploadModelRequest,
    UploadModelOperationMetadata,
    UploadModelResponse,
    GetModelRequest,
    ListModelsRequest,
    ListModelsResponse,
    UpdateModelRequest,
    DeleteModelRequest,
    ExportModelRequest,
    ExportModelOperationMetadata,
    ExportModelResponse,
    GetModelEvaluationRequest,
    ListModelEvaluationsRequest,
    ListModelEvaluationsResponse,
    GetModelEvaluationSliceRequest,
    ListModelEvaluationSlicesRequest,
    ListModelEvaluationSlicesResponse,
)
from .data_item import DataItem
from .dataset_service import (
    CreateDatasetRequest,
    CreateDatasetOperationMetadata,
    GetDatasetRequest,
    UpdateDatasetRequest,
    ListDatasetsRequest,
    ListDatasetsResponse,
    DeleteDatasetRequest,
    ImportDataRequest,
    ImportDataResponse,
    ImportDataOperationMetadata,
    ExportDataRequest,
    ExportDataResponse,
    ExportDataOperationMetadata,
    ListDataItemsRequest,
    ListDataItemsResponse,
    GetAnnotationSpecRequest,
    ListAnnotationsRequest,
    ListAnnotationsResponse,
)


__all__ = (
    "AnnotationSpec",
    "GcsSource",
    "GcsDestination",
    "BigQuerySource",
    "BigQueryDestination",
    "ContainerRegistryDestination",
    "Dataset",
    "ImportDataConfig",
    "ExportDataConfig",
    "ManualBatchTuningParameters",
    "CompletionStats",
    "ModelEvaluationSlice",
    "MachineSpec",
    "DedicatedResources",
    "AutomaticResources",
    "BatchDedicatedResources",
    "ResourcesConsumed",
    "DeployedModelRef",
    "EnvVar",
    "ExplanationMetadata",
    "Explanation",
    "ModelExplanation",
    "Attribution",
    "ExplanationSpec",
    "ExplanationParameters",
    "SampledShapleyAttribution",
    "Model",
    "PredictSchemata",
    "ModelContainerSpec",
    "Port",
    "TrainingPipeline",
    "InputDataConfig",
    "FractionSplit",
    "FilterSplit",
    "PredefinedSplit",
    "TimestampSplit",
    "ModelEvaluation",
    "BatchPredictionJob",
    "CustomJob",
    "CustomJobSpec",
    "WorkerPoolSpec",
    "ContainerSpec",
    "PythonPackageSpec",
    "Scheduling",
    "SpecialistPool",
    "DataLabelingJob",
    "ActiveLearningConfig",
    "SampleConfig",
    "TrainingConfig",
    "Trial",
    "StudySpec",
    "Measurement",
    "HyperparameterTuningJob",
    "CreateCustomJobRequest",
    "GetCustomJobRequest",
    "ListCustomJobsRequest",
    "ListCustomJobsResponse",
    "DeleteCustomJobRequest",
    "CancelCustomJobRequest",
    "CreateDataLabelingJobRequest",
    "GetDataLabelingJobRequest",
    "ListDataLabelingJobsRequest",
    "ListDataLabelingJobsResponse",
    "DeleteDataLabelingJobRequest",
    "CancelDataLabelingJobRequest",
    "CreateHyperparameterTuningJobRequest",
    "GetHyperparameterTuningJobRequest",
    "ListHyperparameterTuningJobsRequest",
    "ListHyperparameterTuningJobsResponse",
    "DeleteHyperparameterTuningJobRequest",
    "CancelHyperparameterTuningJobRequest",
    "CreateBatchPredictionJobRequest",
    "GetBatchPredictionJobRequest",
    "ListBatchPredictionJobsRequest",
    "ListBatchPredictionJobsResponse",
    "DeleteBatchPredictionJobRequest",
    "CancelBatchPredictionJobRequest",
    "UserActionReference",
    "Annotation",
    "GenericOperationMetadata",
    "DeleteOperationMetadata",
    "Endpoint",
    "DeployedModel",
    "PredictRequest",
    "PredictResponse",
    "ExplainRequest",
    "ExplainResponse",
    "CreateEndpointRequest",
    "CreateEndpointOperationMetadata",
    "GetEndpointRequest",
    "ListEndpointsRequest",
    "ListEndpointsResponse",
    "UpdateEndpointRequest",
    "DeleteEndpointRequest",
    "DeployModelRequest",
    "DeployModelResponse",
    "DeployModelOperationMetadata",
    "UndeployModelRequest",
    "UndeployModelResponse",
    "UndeployModelOperationMetadata",
    "CreateTrainingPipelineRequest",
    "GetTrainingPipelineRequest",
    "ListTrainingPipelinesRequest",
    "ListTrainingPipelinesResponse",
    "DeleteTrainingPipelineRequest",
    "CancelTrainingPipelineRequest",
    "CreateSpecialistPoolRequest",
    "CreateSpecialistPoolOperationMetadata",
    "GetSpecialistPoolRequest",
    "ListSpecialistPoolsRequest",
    "ListSpecialistPoolsResponse",
    "DeleteSpecialistPoolRequest",
    "UpdateSpecialistPoolRequest",
    "UpdateSpecialistPoolOperationMetadata",
    "UploadModelRequest",
    "UploadModelOperationMetadata",
    "UploadModelResponse",
    "GetModelRequest",
    "ListModelsRequest",
    "ListModelsResponse",
    "UpdateModelRequest",
    "DeleteModelRequest",
    "ExportModelRequest",
    "ExportModelOperationMetadata",
    "ExportModelResponse",
    "GetModelEvaluationRequest",
    "ListModelEvaluationsRequest",
    "ListModelEvaluationsResponse",
    "GetModelEvaluationSliceRequest",
    "ListModelEvaluationSlicesRequest",
    "ListModelEvaluationSlicesResponse",
    "DataItem",
    "CreateDatasetRequest",
    "CreateDatasetOperationMetadata",
    "GetDatasetRequest",
    "UpdateDatasetRequest",
    "ListDatasetsRequest",
    "ListDatasetsResponse",
    "DeleteDatasetRequest",
    "ImportDataRequest",
    "ImportDataResponse",
    "ImportDataOperationMetadata",
    "ExportDataRequest",
    "ExportDataResponse",
    "ExportDataOperationMetadata",
    "ListDataItemsRequest",
    "ListDataItemsResponse",
    "GetAnnotationSpecRequest",
    "ListAnnotationsRequest",
    "ListAnnotationsResponse",
)

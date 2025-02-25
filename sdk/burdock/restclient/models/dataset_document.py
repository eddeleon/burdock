# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DatasetDocument(Model):
    """DatasetDocument.

    :param dataset_type: The type of the dataset
    :type dataset_type: str
    :param csv_details:
    :type csv_details: ~restclient.models.LocalCSVDetails
    """

    _attribute_map = {
        'dataset_type': {'key': 'dataset_type', 'type': 'str'},
        'csv_details': {'key': 'csv_details', 'type': 'LocalCSVDetails'},
    }

    def __init__(self, dataset_type=None, csv_details=None):
        super(DatasetDocument, self).__init__()
        self.dataset_type = dataset_type
        self.csv_details = csv_details

# coding: utf-8

"""
    应用存储  API 文档

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from PMCore.Client.api.file_api import FileApi


class TestFileApi(unittest.TestCase):
    """FileApi unit test stubs"""

    def setUp(self) -> None:
        self.api = FileApi()

    def tearDown(self) -> None:
        pass

    def test_file_create_folder(self) -> None:
        """Test case for file_create_folder

        创建文件夹
        """
        pass

    def test_file_delete(self) -> None:
        """Test case for file_delete

        删除文件
        """
        pass

    def test_file_rename(self) -> None:
        """Test case for file_rename

        重命名文件
        """
        pass

    def test_file_upload(self) -> None:
        """Test case for file_upload

        上传文件
        """
        pass

    def test_files(self) -> None:
        """Test case for files

        文件列表
        """
        pass


if __name__ == '__main__':
    unittest.main()

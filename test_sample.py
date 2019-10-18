# Using Pytest framework for unit testing. Then expanding in to more functional testing. Currently
# testing three functions from fileOne.py. Showing both a pass and failed tests for each function.
#
import pytest
import pymongo
import main
import login
from functions import read_document, create_document, update_document, delete_document
    

# Testing Crud function read_document (PASS)
def test_read_documnet_good():
    assert (read_document({"_id": 149})['name']) == 'Synthia Labelle'
    
# Testing Crud function read_document (FAIL)
def test_read_document_failed_test():
    assert (read_document({"_id": 149})['name']) == 'jerry Reed'

# Testing Crud function create_document (PASS)
def test_create_document_passed_test():
    assert (create_document({"_id": 500,"name": 'first last'})) == None

# Testing Crud function create_document (FAIL)
def test_create_document_failed_test():
    assert (create_document({"_id": "No numbers","name": 'user'})) == False

# Testing Crud function delete_document (PASS)
def test_delete_document_passed_test():
    delete_document({"_id": 500})
    assert(read_document({"_id": 500})) == None

# Testing Crud function delete_document (FAIL)
def test_delete_document_failed_test():
    assert (delete_document({"_id": 600})) == None

# Testing Crud function delete_document (PASS)
def test_update_document_passed_test():
    create_document({"_id": 500,"name": 'first last'})

    new_update_query = 500
    new_update_value = {"$set":{"test field": "new_value"}}
    assert(update_document(new_update_query,new_update_value)) == None




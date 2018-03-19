#coding:utf-8
class global_var:#在excel里的列号
	#case_id
	caseId = '0'
	request_name = '1'
	url = '2'
	is_run = '3'
	request_method = '4'
	header = '5'
	caseid_depend = '6'
	responseData_depend = '7'
	dataField_depend = '8'
	request_data = '9'
	expected_result = '10'
	actual_result = '11'
#获取caseid
def get_caseId():
		return global_var.caseId

#获取url
def get_url():
		return global_var.url

def get_isRun():
	return global_var.is_run

def get_request_method():
	return global_var.request_method

def get_header():
	return global_var.header

def get_case_depend():
	return global_var.caseid_depend

def get_data_depend():
	return global_var.responseData_depend

def get_field_depend():
	return global_var.dataField_depend

def get_request_data():
	return global_var.request_data

def get_expect_result():
	return global_var.expected_result

def get_actual_result():
	return global_var.actual_result



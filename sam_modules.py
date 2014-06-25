# coding=utf-8
# !/usr/bin/python
"""
__synopsis__    : Contains basic functionality like taking user input, opening
                  file
__description__ :
__project__     : dip
__author__      : Samujjwal_Ghosh
__version__     : " 1.0 "
__date__        : "25-Jun-14"
__copyright__   : "Copyright (c) 2014 Samujjwal_Ghosh"
__license__     : "Python"

__classes__     :
    ReturnValue(object) : Contains return values of the call to sam_modules
        call_stack = []
        __init__(string, object=None, string='', string='')

__variables__   :
    call_pass = string : represents call pass
    call_fail = string : represents call fail
    call_err  = string : represents call error

__methods__     :
    is_empty (list) :
    check_params (tuple, tuple, tuple) : check parameters types
    int_input (string) : takes integer input from console
    str_input (string) : takes string input from console
    open_file (string, string='r', string=None, int=0, int=0) : opens file
    print_log (string) : prints to console and logs to a file

"""

import os
import types
import inspect


call_pass = 'PASS'
call_fail = 'FAIL'
call_err = 'ERROR'


class ReturnValue(object):
    """
    Contains return values of the call
    """

    call_stack = []

    def __init__(self, call_status, val=None, msg='', method_msg=''):
        self.call_status = call_status
        self.msg = msg
        self.val = val
        self.val_type = type(val)
        self.method_msg = method_msg


def is_empty(param_list):
    """

    :param param_list:
    :return:
    """
    method_name = '##' + os.path.basename(__file__) + ':is_empty: '
    print method_name
    ReturnValue.call_stack.append(method_name)

    msg = "[%s]: non-empty" % inspect.currentframe().f_back.f_lineno

    if not param_list.__len__():
        msg = "[%s]: Empty value provided for <param_list>."
        return ReturnValue(call_status=call_err, msg=msg)
    elif param_list.__len__() == 1:
        if param_list:
            msg = "[%s]: [%s] non-empty." % (inspect.currentframe(
            ).f_back.f_lineno, param_list)
            return ReturnValue(call_status=call_pass, msg=msg)
        else:
            msg = "[%s]: [%s] Empty." % (
                inspect.currentframe().f_back.f_lineno, param_list)
            return ReturnValue(call_status=call_fail, msg=msg)
    else:
        for param in param_list:
            if not param:
                msg = "[%s]: Empty value provided for parameter [%s]" %\
                      inspect.currentframe().f_back.f_lineno, param
                return ReturnValue(call_status=call_fail, msg=msg)
    return ReturnValue(call_status=call_fail, msg=msg)


def check_params(param_values, param_types, required):
    """
    checks the parameter types
    :param required:
        Type: tuple
        Required
        Read Only
    :param param_values:
        Type: tuple
        Required
        Read Only
    :param param_types:
        Type: tuple
        Required
        Read Only
    :return Object: return object of type [ReturnValue]
        Type: object
    """
    method_name = '##' + os.path.basename(__file__) + ':check_params: '
    print method_name
    ReturnValue.call_stack.append(method_name)

    if not (param_values.__len__() == param_types.__len__() ==
            required.__len__()):
        print "Length of param lists passed are not same."
        msg = "Length of param lists passed are not same."
        return ReturnValue(call_status=call_err, msg=msg)

    if (not isinstance(param_values, types.TupleType)) or (
            not isinstance(param_types, types.TupleType)) or (
            not isinstance(required, types.TupleType)):
        print "[%s]: Provided parameters are not <tuple> type." %\
              inspect.currentframe().f_back.f_lineno
        msg = "[%s]: Provided parameters are not <tuple> type." %\
              inspect.currentframe().f_back.f_lineno
        return ReturnValue(call_status=call_err, msg=msg)

    if (not param_values) or (not param_types) or (not required):
        print "[%s]: Empty tuple list provided for Required "\
              "parameter." % inspect.currentframe().f_back.f_lineno
        msg = "[%s]: Empty tuple list provided for Required "\
              "parameter." % inspect.currentframe().f_back.f_lineno
        return ReturnValue(call_status=call_err, msg=msg)
    i = 0
    for param_val, param_type in zip(param_values, param_types):
        if not param_val:
            if required[i] == 1:
                msg = "Empty value provided for required parameter no: [%d]."\
                      % i
                return ReturnValue(call_status=call_fail, val=i, msg=msg)

        if type(param_val) != getattr(types, param_type):  # checking type
            # of param_val with builtin types of module types for all elements
            msg = "[%s]: Type mismatch for param no: [%d]; Expected: [%s]"\
                  " Provided: [%s]" % (
                      inspect.currentframe().f_back.f_lineno, i, param_type,
                      type(param_val))
            return ReturnValue(call_status=call_fail, val=i, msg=msg)
        i += 1
    return ReturnValue(call_status=call_pass, msg='Type check successful for '
                                                  'all parameters.')


def int_input(to_print):
    """
    Takes integer input from console
    :param to_print: Prints
        Type: str
        Required
        Read Only
    :return Object: return object of type [ReturnValue]
        Type: object
    """
    method_name = '##' + os.path.basename(__file__) + ':int_input: '
    print method_name
    ReturnValue.call_stack.append(method_name)

    if not to_print:
        msg = "Empty string passed."
        return ReturnValue(call_status=call_err, msg=msg)

    tc = check_params(tuple([to_print]),
                      tuple(['StringType']),
                      tuple([1]))
    if (tc.call_status == call_fail) or (tc.call_status == call_err):
        return ReturnValue(call_status=tc.call_status, msg=tc.msg)

    while 1:
        try:
            val = int(raw_input(to_print))
            msg = "[%s]: Retrieved value [%s] successfully." % (
                inspect.currentframe().f_back.f_lineno, val)
            return ReturnValue(call_status=call_pass, val=val, msg=msg)
        except ValueError:
            retry = raw_input("Empty or non-integer value entered; retry? ("
                              "y/n; default:n): ")
            if retry == 'y':
                continue
            else:
                msg = "[%s]: Entered [%s]." % (
                    inspect.currentframe().f_back.f_lineno, retry)
                return ReturnValue(call_status=call_fail, msg=msg)


def str_input(to_print):
    """
    Takes string input from console
    :param to_print: Prints
        Type: str
        Required
        Read Only
    :return Object: return object of type [ReturnValue]
        Type: object
    """
    method_name = '##' + os.path.basename(__file__) + ':str_input: '
    print method_name
    ReturnValue.call_stack.append(method_name)

    if not to_print:
        msg = "Empty string passed."
        return ReturnValue(call_status=call_err, msg=msg)

    tc = check_params(tuple([to_print]),
                      tuple(['StringType']),
                      tuple([1]))
    if (tc.call_status == call_fail) or (tc.call_status == call_err):
        return ReturnValue(call_status=tc.call_status, msg=tc.msg)

    while 1:
        val = raw_input(to_print)
        if val == "":
            retry = raw_input("Empty value entered; retry? (y/n; default:n): ")
            if retry == 'y':
                continue
            else:
                msg = "[%s]: Entered [%s]." % (
                    inspect.currentframe().f_back.f_lineno, retry)
                return ReturnValue(call_fail, msg=msg)
        return ReturnValue(call_pass, val=val)


def open_file(file_name, mode='r', content=None, print_file=0, close=0):
    """
    takes file name check its existence and returns file handle
    :param close: closes the file after operation.
        Type: int
        Optional
        Read Only
        Default: 0
    :param print_file: if 1, then prints the content of file if mode contain [r]
        Type: int
        Optional
        Read Only
        Default: 0
    :param content: if not None, then append / writes [content] to the file if
        mode contains 'a' / 'w' and is not 'r'.
        Type: str
        Optional
        Read Only
        Default: None
    :param file_name: Name of the file to open.
        Type: str
        Required
        Read Only
    :param mode: File opening mode.
        Type: str
        Optional
        Read Only
        Default: 'r'
    :return Object: returns file handle within object of [ReturnValue]
        Type: object
    """
    method_name = '##' + os.path.basename(__file__) + ':open_file: '
    print method_name
    ReturnValue.call_stack.append(method_name)

    check_params(tuple([file_name, mode, content, print_file, close]),
                 tuple(['StringType', 'StringType', 'StringType', 'IntType',
                        'IntType']),
                 tuple([1, 0, 0, 0, 0]))

    if print_file and mode.find('r') != -1:
        if os.path.isfile(file_name) and os.access(file_name, os.R_OK):
            # we are reading the file only if mode contains [r]
            # will only execute if file exists and accessible
            # find() returns -1 when string not found
            if mode.find('b') != -1:  # will open in binary if mode contains [b]
                i_mode = 'rb'
                p_m = "Printing file [%s] in binary mode: " % file_name
            else:
                i_mode = 'r'
                p_m = "Printing file [%s] in text mode: " % file_name
            try:  # opening the file in read mode to print the file
                val = open(file_name, i_mode)
                print p_m
            except IOError as err:
                msg = "Could not read file [%s]; [%s] occurred." % (
                    file_name, err)
                return ReturnValue(call_err, msg=msg)
            try:  # printing the file
                print "[%s]" % val.read()
            except IOError as err:
                print "Unable to read file; [%s] occurred." % err
            val.close()
        else:
            print "File [%s] does not exist; can not print." % file_name

    try:
        val = open(file_name, mode)
        msg = "Opened file [%s] successfully." % file_name
    except IOError as err:
        msg = "Failed to open file [%s]; [%s] occurred." % (file_name, err)
        return ReturnValue(call_err, msg=msg)
    except ValueError as err:
        msg = "Failed to open file [%s] with mode [%s]; [%s] occurred." % (
            file_name, mode, err)
        return ReturnValue(call_fail, msg=msg)

    if content and (mode.lower() != 'r' or mode.lower() != 'rb'):  # will write
        # only if content is defined and mode is not 'r' or 'rb'
        print "writing content to file [%s]." % file_name
        try:
            val.write(content)
            msg = 'Written content successfully.'
        except IOError as err:
            msg = "Failed to write to file [%s]; [%s] occurred." % (
                file_name, err)
            val.close()
            return ReturnValue(call_fail, msg=msg)
    if close:
        val.close()
        val = None
        msg = "Operation successful and file [%s] closed." % file_name
    return ReturnValue(call_pass, val=val, msg=msg)


def print_log(log_string, log_only=0):
    """
    Prints to console and logs to a file
    :param log_only: will not print if 1
        Type: int
        Optional
        Read Only
    :param log_string: string to log in file <sam_modules_log.txt>
        Type: str
        Required
        Read Only
    :return Object: return object of type [ReturnValue]
        Type: object
    """
    method_name = '##' + os.path.basename(__file__) + ':print_log: '
    print method_name
    ReturnValue.call_stack.append(method_name)

    if not log_string:
        msg = "Empty string passed."
        return ReturnValue(call_status=call_err, msg=msg)

    tc = check_params(tuple([log_string]),
                      tuple(['StringType']),
                      tuple([1]))
    if (tc.call_status == call_fail) or (tc.call_status == call_err):
        return ReturnValue(call_status=tc.call_status, msg=tc.msg)

    if __name__ == "__main__":  # will always print when unit testing
        log_only = 1

    if log_only == 0:
        print log_string
    open_file(file_name='sam_modules_log.txt', mode='a+', content=log_string,
              close=1)
    msg = 'Logged successfully.'
    return ReturnValue(call_pass, val=1, msg=msg)


if __name__ == "__main__":  # for unit testing purposes only; will not execute
    # if module API call.
    # user_input = int_input("Enter a number: ")
    # user_input = str_input('Enter a string: ')
    # print user_input.call_stack
    # print user_input.call_status
    # print user_input.msg
    #print user_input.val

    # print str_input("Enter a string: ")
    # from time import ctime
    # print str(ctime())
    # f = open_file('READ.txt', "w+", "samujjwal\n", print_file=1)
    # print f.call_status
    # print f.msg

    pl = print_log('logging...', log_only=0)

    # f = open('hello.txt', 'w+')
    #
    # f.close()
    # f = open('hello.txt', 'r')
    # print f.read()
    # f.write("hello")

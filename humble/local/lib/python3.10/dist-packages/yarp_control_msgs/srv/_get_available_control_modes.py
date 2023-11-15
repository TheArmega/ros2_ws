# generated from rosidl_generator_py/resource/_idl.py.em
# with input from yarp_control_msgs:srv/GetAvailableControlModes.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_GetAvailableControlModes_Request(type):
    """Metaclass of message 'GetAvailableControlModes_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('yarp_control_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'yarp_control_msgs.srv.GetAvailableControlModes_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__get_available_control_modes__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__get_available_control_modes__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__get_available_control_modes__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__get_available_control_modes__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__get_available_control_modes__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class GetAvailableControlModes_Request(metaclass=Metaclass_GetAvailableControlModes_Request):
    """Message class 'GetAvailableControlModes_Request'."""

    __slots__ = [
        '_only_implemented',
    ]

    _fields_and_field_types = {
        'only_implemented': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.only_implemented = kwargs.get('only_implemented', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.only_implemented != other.only_implemented:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def only_implemented(self):
        """Message field 'only_implemented'."""
        return self._only_implemented

    @only_implemented.setter
    def only_implemented(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'only_implemented' field must be of type 'bool'"
        self._only_implemented = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_GetAvailableControlModes_Response(type):
    """Metaclass of message 'GetAvailableControlModes_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('yarp_control_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'yarp_control_msgs.srv.GetAvailableControlModes_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__get_available_control_modes__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__get_available_control_modes__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__get_available_control_modes__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__get_available_control_modes__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__get_available_control_modes__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'RESPONSE__DEFAULT': 'NOT_SPECIFIED',
        }

    @property
    def RESPONSE__DEFAULT(cls):
        """Return default value for message field 'response'."""
        return 'NOT_SPECIFIED'


class GetAvailableControlModes_Response(metaclass=Metaclass_GetAvailableControlModes_Response):
    """Message class 'GetAvailableControlModes_Response'."""

    __slots__ = [
        '_modes',
        '_response',
        '_opt_descr',
    ]

    _fields_and_field_types = {
        'modes': 'sequence<string>',
        'response': 'string',
        'opt_descr': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.modes = kwargs.get('modes', [])
        self.response = kwargs.get(
            'response', GetAvailableControlModes_Response.RESPONSE__DEFAULT)
        self.opt_descr = kwargs.get('opt_descr', str())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.modes != other.modes:
            return False
        if self.response != other.response:
            return False
        if self.opt_descr != other.opt_descr:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def modes(self):
        """Message field 'modes'."""
        return self._modes

    @modes.setter
    def modes(self, value):
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, str) for v in value) and
                 True), \
                "The 'modes' field must be a set or sequence and each value of type 'str'"
        self._modes = value

    @builtins.property
    def response(self):
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'response' field must be of type 'str'"
        self._response = value

    @builtins.property
    def opt_descr(self):
        """Message field 'opt_descr'."""
        return self._opt_descr

    @opt_descr.setter
    def opt_descr(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'opt_descr' field must be of type 'str'"
        self._opt_descr = value


class Metaclass_GetAvailableControlModes(type):
    """Metaclass of service 'GetAvailableControlModes'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('yarp_control_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'yarp_control_msgs.srv.GetAvailableControlModes')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__get_available_control_modes

            from yarp_control_msgs.srv import _get_available_control_modes
            if _get_available_control_modes.Metaclass_GetAvailableControlModes_Request._TYPE_SUPPORT is None:
                _get_available_control_modes.Metaclass_GetAvailableControlModes_Request.__import_type_support__()
            if _get_available_control_modes.Metaclass_GetAvailableControlModes_Response._TYPE_SUPPORT is None:
                _get_available_control_modes.Metaclass_GetAvailableControlModes_Response.__import_type_support__()


class GetAvailableControlModes(metaclass=Metaclass_GetAvailableControlModes):
    from yarp_control_msgs.srv._get_available_control_modes import GetAvailableControlModes_Request as Request
    from yarp_control_msgs.srv._get_available_control_modes import GetAvailableControlModes_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
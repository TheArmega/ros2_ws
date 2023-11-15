// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from yarp_control_msgs:msg/Velocity.idl
// generated code does not contain a copyright notice

#ifndef YARP_CONTROL_MSGS__MSG__DETAIL__VELOCITY__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define YARP_CONTROL_MSGS__MSG__DETAIL__VELOCITY__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "yarp_control_msgs/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "yarp_control_msgs/msg/detail/velocity__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace yarp_control_msgs
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_yarp_control_msgs
cdr_serialize(
  const yarp_control_msgs::msg::Velocity & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_yarp_control_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  yarp_control_msgs::msg::Velocity & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_yarp_control_msgs
get_serialized_size(
  const yarp_control_msgs::msg::Velocity & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_yarp_control_msgs
max_serialized_size_Velocity(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace yarp_control_msgs

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_yarp_control_msgs
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, yarp_control_msgs, msg, Velocity)();

#ifdef __cplusplus
}
#endif

#endif  // YARP_CONTROL_MSGS__MSG__DETAIL__VELOCITY__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
// Generated by gencpp from file face_detector/face_msgs.msg
// DO NOT EDIT!


#ifndef FACE_DETECTOR_MESSAGE_FACE_MSGS_H
#define FACE_DETECTOR_MESSAGE_FACE_MSGS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <face_detector/my_list.h>

namespace face_detector
{
template <class ContainerAllocator>
struct face_msgs_
{
  typedef face_msgs_<ContainerAllocator> Type;

  face_msgs_()
    : index(0)
    , location()  {
    }
  face_msgs_(const ContainerAllocator& _alloc)
    : index(0)
    , location(_alloc)  {
  (void)_alloc;
    }



   typedef int16_t _index_type;
  _index_type index;

   typedef std::vector< ::face_detector::my_list_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::face_detector::my_list_<ContainerAllocator> >::other >  _location_type;
  _location_type location;





  typedef boost::shared_ptr< ::face_detector::face_msgs_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::face_detector::face_msgs_<ContainerAllocator> const> ConstPtr;

}; // struct face_msgs_

typedef ::face_detector::face_msgs_<std::allocator<void> > face_msgs;

typedef boost::shared_ptr< ::face_detector::face_msgs > face_msgsPtr;
typedef boost::shared_ptr< ::face_detector::face_msgs const> face_msgsConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::face_detector::face_msgs_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::face_detector::face_msgs_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace face_detector

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'face_detector': ['/home/beta/Desktop/face_detect_ws/src/face_detector/msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::face_detector::face_msgs_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::face_detector::face_msgs_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::face_detector::face_msgs_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::face_detector::face_msgs_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::face_detector::face_msgs_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::face_detector::face_msgs_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::face_detector::face_msgs_<ContainerAllocator> >
{
  static const char* value()
  {
    return "8b8cdd61744da60b1fa004570af7b850";
  }

  static const char* value(const ::face_detector::face_msgs_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x8b8cdd61744da60bULL;
  static const uint64_t static_value2 = 0x1fa004570af7b850ULL;
};

template<class ContainerAllocator>
struct DataType< ::face_detector::face_msgs_<ContainerAllocator> >
{
  static const char* value()
  {
    return "face_detector/face_msgs";
  }

  static const char* value(const ::face_detector::face_msgs_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::face_detector::face_msgs_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int16 index\n"
"my_list[] location\n"
"\n"
"================================================================================\n"
"MSG: face_detector/my_list\n"
"#list 5D\n"
"string lable\n"
"int16 top\n"
"int16 right\n"
"int16 bottom \n"
"int16 left\n"
"\n"
;
  }

  static const char* value(const ::face_detector::face_msgs_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::face_detector::face_msgs_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.index);
      stream.next(m.location);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct face_msgs_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::face_detector::face_msgs_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::face_detector::face_msgs_<ContainerAllocator>& v)
  {
    s << indent << "index: ";
    Printer<int16_t>::stream(s, indent + "  ", v.index);
    s << indent << "location[]" << std::endl;
    for (size_t i = 0; i < v.location.size(); ++i)
    {
      s << indent << "  location[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::face_detector::my_list_<ContainerAllocator> >::stream(s, indent + "    ", v.location[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // FACE_DETECTOR_MESSAGE_FACE_MSGS_H

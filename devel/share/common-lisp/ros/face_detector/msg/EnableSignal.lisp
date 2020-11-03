; Auto-generated. Do not edit!


(cl:in-package face_detector-msg)


;//! \htmlinclude EnableSignal.msg.html

(cl:defclass <EnableSignal> (roslisp-msg-protocol:ros-message)
  ((enable
    :reader enable
    :initarg :enable
    :type cl:fixnum
    :initform 0))
)

(cl:defclass EnableSignal (<EnableSignal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <EnableSignal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'EnableSignal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name face_detector-msg:<EnableSignal> is deprecated: use face_detector-msg:EnableSignal instead.")))

(cl:ensure-generic-function 'enable-val :lambda-list '(m))
(cl:defmethod enable-val ((m <EnableSignal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader face_detector-msg:enable-val is deprecated.  Use face_detector-msg:enable instead.")
  (enable m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <EnableSignal>) ostream)
  "Serializes a message object of type '<EnableSignal>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'enable)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <EnableSignal>) istream)
  "Deserializes a message object of type '<EnableSignal>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'enable)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<EnableSignal>)))
  "Returns string type for a message object of type '<EnableSignal>"
  "face_detector/EnableSignal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'EnableSignal)))
  "Returns string type for a message object of type 'EnableSignal"
  "face_detector/EnableSignal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<EnableSignal>)))
  "Returns md5sum for a message object of type '<EnableSignal>"
  "34abd7794638063ef7576ad13e0da876")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'EnableSignal)))
  "Returns md5sum for a message object of type 'EnableSignal"
  "34abd7794638063ef7576ad13e0da876")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<EnableSignal>)))
  "Returns full string definition for message of type '<EnableSignal>"
  (cl:format cl:nil "uint8 enable~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'EnableSignal)))
  "Returns full string definition for message of type 'EnableSignal"
  (cl:format cl:nil "uint8 enable~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <EnableSignal>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <EnableSignal>))
  "Converts a ROS message object to a list"
  (cl:list 'EnableSignal
    (cl:cons ':enable (enable msg))
))

; Auto-generated. Do not edit!


(cl:in-package diff_drive-msg)


;//! \htmlinclude GoToPoseGoal.msg.html

(cl:defclass <GoToPoseGoal> (roslisp-msg-protocol:ros-message)
  ((pose
    :reader pose
    :initarg :pose
    :type geometry_msgs-msg:PoseStamped
    :initform (cl:make-instance 'geometry_msgs-msg:PoseStamped)))
)

(cl:defclass GoToPoseGoal (<GoToPoseGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GoToPoseGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GoToPoseGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name diff_drive-msg:<GoToPoseGoal> is deprecated: use diff_drive-msg:GoToPoseGoal instead.")))

(cl:ensure-generic-function 'pose-val :lambda-list '(m))
(cl:defmethod pose-val ((m <GoToPoseGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader diff_drive-msg:pose-val is deprecated.  Use diff_drive-msg:pose instead.")
  (pose m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GoToPoseGoal>) ostream)
  "Serializes a message object of type '<GoToPoseGoal>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pose) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GoToPoseGoal>) istream)
  "Deserializes a message object of type '<GoToPoseGoal>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pose) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GoToPoseGoal>)))
  "Returns string type for a message object of type '<GoToPoseGoal>"
  "diff_drive/GoToPoseGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GoToPoseGoal)))
  "Returns string type for a message object of type 'GoToPoseGoal"
  "diff_drive/GoToPoseGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GoToPoseGoal>)))
  "Returns md5sum for a message object of type '<GoToPoseGoal>"
  "3f8930d968a3e84d471dff917bb1cdae")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GoToPoseGoal)))
  "Returns md5sum for a message object of type 'GoToPoseGoal"
  "3f8930d968a3e84d471dff917bb1cdae")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GoToPoseGoal>)))
  "Returns full string definition for message of type '<GoToPoseGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# goal definition~%geometry_msgs/PoseStamped pose~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GoToPoseGoal)))
  "Returns full string definition for message of type 'GoToPoseGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# goal definition~%geometry_msgs/PoseStamped pose~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GoToPoseGoal>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pose))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GoToPoseGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'GoToPoseGoal
    (cl:cons ':pose (pose msg))
))

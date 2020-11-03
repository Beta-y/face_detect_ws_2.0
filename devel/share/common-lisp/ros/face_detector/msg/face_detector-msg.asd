
(cl:in-package :asdf)

(defsystem "face_detector-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "EnableSignal" :depends-on ("_package_EnableSignal"))
    (:file "_package_EnableSignal" :depends-on ("_package"))
    (:file "face_msgs" :depends-on ("_package_face_msgs"))
    (:file "_package_face_msgs" :depends-on ("_package"))
    (:file "my_list" :depends-on ("_package_my_list"))
    (:file "_package_my_list" :depends-on ("_package"))
  ))
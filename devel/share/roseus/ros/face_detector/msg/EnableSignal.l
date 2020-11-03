;; Auto-generated. Do not edit!


(when (boundp 'face_detector::EnableSignal)
  (if (not (find-package "FACE_DETECTOR"))
    (make-package "FACE_DETECTOR"))
  (shadow 'EnableSignal (find-package "FACE_DETECTOR")))
(unless (find-package "FACE_DETECTOR::ENABLESIGNAL")
  (make-package "FACE_DETECTOR::ENABLESIGNAL"))

(in-package "ROS")
;;//! \htmlinclude EnableSignal.msg.html


(defclass face_detector::EnableSignal
  :super ros::object
  :slots (_enable ))

(defmethod face_detector::EnableSignal
  (:init
   (&key
    ((:enable __enable) 0)
    )
   (send-super :init)
   (setq _enable (round __enable))
   self)
  (:enable
   (&optional __enable)
   (if __enable (setq _enable __enable)) _enable)
  (:serialization-length
   ()
   (+
    ;; uint8 _enable
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _enable
       (write-byte _enable s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _enable
     (setq _enable (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get face_detector::EnableSignal :md5sum-) "34abd7794638063ef7576ad13e0da876")
(setf (get face_detector::EnableSignal :datatype-) "face_detector/EnableSignal")
(setf (get face_detector::EnableSignal :definition-)
      "uint8 enable

")



(provide :face_detector/EnableSignal "34abd7794638063ef7576ad13e0da876")



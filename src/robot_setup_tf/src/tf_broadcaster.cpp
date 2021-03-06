#include <ros/ros.h>
#include <tf/transform_broadcaster.h>

int main(int argc, char** argv){
  ros::Time t = ros::Time(0);
  ros::init(argc, argv, "robot_tf_publisher");
  ros::NodeHandle n;

  ros::Rate r(100);

  tf::TransformBroadcaster broadcaster_scan2;
  tf::TransformBroadcaster broadcaster_scan1;
  tf::TransformBroadcaster broadcaster_scanMulti;
  tf::TransformBroadcaster broadcaster_realSense;

  while(n.ok()){
    broadcaster_scan1.sendTransform(
      tf::StampedTransform(
        //(0,0,-3.923) OG
        tf::Transform(tf::createQuaternionFromRPY(0,0,3.14159 - 3.14159/4.0), tf::Vector3(-0.1765, 0.1765, 0.150)),
        ros::Time::now(),"base_link", "base_omron1"));
    broadcaster_scan2.sendTransform(
      tf::StampedTransform(
        //(0,0,-0.785) OG
        tf::Transform(tf::createQuaternionFromRPY(0,0,-3.14159/4.0), tf::Vector3(0.1765, -0.1765, 0.150)),
        ros::Time::now(),"base_link", "base_omron2"));
    broadcaster_scan2.sendTransform(
      tf::StampedTransform(
        tf::Transform(tf::createQuaternionFromRPY(0,0,0), tf::Vector3(0.0, -0.0, 0.150)),
        ros::Time::now(),"base_link", "base_laser_link"));
    broadcaster_realSense.sendTransform(
      tf::StampedTransform(
        tf::Transform(tf::createQuaternionFromRPY(3.14159,0,0), tf::Vector3(0.2150, 0, 0.25)),
        ros::Time::now(),"base_link", "camera_link"));
	r.sleep();
  }
}

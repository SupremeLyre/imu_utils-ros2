from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription(
        [
            DeclareLaunchArgument("imu_topic", default_value="/gici/imu_raw"),
            DeclareLaunchArgument("imu_name", default_value="ADIS16475"),
            DeclareLaunchArgument(
                "data_save_path",
                default_value=PathJoinSubstitution(
                    [FindPackageShare("imu_utils2"), "data"]
                ),
            ),
            DeclareLaunchArgument("max_time_min", default_value="300"),
            DeclareLaunchArgument("max_cluster", default_value="100"),
            Node(
                package="imu_utils2",
                executable="imu_an",
                name="imu_analysis",
                output="screen",  # 添加这一行，将输出显示到控制台
                parameters=[
                    {
                        "imu_topic": "/gici/imu_raw",
                        "imu_name": "ADIS16475",
                        "data_save_path": PathJoinSubstitution(
                            [FindPackageShare("imu_utils2"), "data"]
                        ),
                        "max_time_min": 300,
                        "max_cluster": 100,
                    }
                ],
            ),
        ]
    )

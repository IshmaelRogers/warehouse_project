from launch import LaunchDescription, LaunchConfiguration
from launch_ros.actions import Node

map_file = LaunchConfiguration('map_file')

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='nav2_map_server',
            executable='map_server',
            name='map_server',
            output='screen',
            parameters=[{'use_sim_time': True},{'yaml_filename': 'config/warehouse_map_sim.yaml'}]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', 'config/rviz_config.rviz']
        ),
        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager',
            output='screen',
            parameters=[{'use_sim_time': True},{'autostart': True, 'node_names': ['map_server']}]
        ),
    ])

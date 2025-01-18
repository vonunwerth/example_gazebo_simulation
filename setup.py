from setuptools import find_packages, setup
import os

package_name = 'example_gazebo_simulation'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Hinzufügen der Ordner
        ('share/' + package_name + '/config', ['config/' + f for f in os.listdir('config')]),
        ('share/' + package_name + '/description', ['description/' + f for f in os.listdir('description')]),
        ('share/' + package_name + '/launch', ['launch/' + f for f in os.listdir('launch')]),
        ('share/' + package_name + '/worlds', ['worlds/' + f for f in os.listdir('worlds')]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='max',
    maintainer_email='maximilian.von.unwerth@tu-berlin.de',
    description='A simple gazebo simulation with ros2_control',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)


from setuptools import find_packages, setup

package_name = 'a_learn'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='charansc',
    maintainer_email='charanvssc@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'pub_node=a_learn.my_first_node:main',
        'sub_node=a_learn.my_first_sub:main',
        'turtlesim_teleop=a_learn.turtlesim_teleop:main',
        
        'para_test=a_learn.para_node:main',
        'service_client=a_learn.add_service_client:main',
        'service_add=a_learn.service_test_add:main',
        ],
    },
)

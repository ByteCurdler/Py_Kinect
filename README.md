# Py_Kinect
A bridge so you can connect Python 2 and Python 3.
Supports types `int` and `float`.
# Usage
### Initialization:
```python3
>>> from kinect import import2
>>> module = import2("module_name")
```
You can now use `module` as your module.
### Example usage:
```python3
>>> from kinect import import2
>>> test = import2("test")
>>> test.cat
123
>>> test.pi
3.14
>>> test.name
"test"
>>> test.Cat.dog
"no"
>>> 
```

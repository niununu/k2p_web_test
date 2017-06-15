###添加新功能
src下添加功能，修改__init.py__文件
data下添加功能，修改__init.py__文件

遍历数组：
```python
for x in xrange(0,len(data)):
	data[x]['action'] = 'add'
	portForward.main(data[x])
	time.sleep(sleepTime)
```
遍历字典
```python
for key in data:
	fileObject.write('\t%s = %s\n' % (key, data[key]))
```

单独运行某个脚本时进入的主函数
```python
if __name__ == '__main__':
	pass
```
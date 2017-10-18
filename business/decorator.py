# -*- coding: utf-8 -*-

class cached_context_property(property):
    """用于指定一个可以被context缓存的decorator

    ```
    @cached_context_property
    def name(self):
    	return 'hello ' + 'world'
    ```

    当我们调用`self.name`之后，`self.context['name'] = 'hello world'`，后续访问`self.name`，会直接从`self.context`中获取
    """

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        property.__init__(self, fget, fset, fdel, doc)

        self.func = fget
        self.func_name = fget.__name__

    def __get__(self, instance, type=None):
        if instance is None:
            return self

        value = instance.context.get(self.func_name, None)
        if value == None:
            value = self.func(instance)
            instance.context[self.func_name] = value
        return value

    def __set__(self, instance, value):
        instance.context[self.func_name] = value
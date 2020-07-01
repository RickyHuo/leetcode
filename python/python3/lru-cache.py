# encoding: utf-8
import json

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = None
        self.final = None
        self.capacity = capacity
        self.data = {}

    def _last_key(self, key):
        return self.data[key]["last"]

    def _next_key(self, key):
        return self.data[key]["next"]

    def _last_value(self, key):
        return self.data[self.data[key]["last"]]

    def _next_value(self, key):
        return self.data[self.data[key]["next"]]

    def _refacotr(self, key):
        """
        拿到一个活跃的key，重构双向链表
        :param key:
        :return:
        """
        if len(self.data) == 1:
            self.head = key
            self.final = key
            return
        elif self.final == key:
            return

        # 前缀next指向后缀
        if self._last_key(key) is not None:
            self._last_value(key)["next"] = self._next_key(key)
        else:
            self.head = self._next_key(key)

        # 后缀last指向前缀
        if self._next_key(key) is not None:
            self._next_value(key)["last"] = self._last_key(key)
        else:
            return

        # final节点的Next指向key
        self.data[self.final]["next"] = key
        #
        self.data[key]["last"] = self.final
        # last节点指向key
        self.final = key
        # key 对应的Next置空
        self.data[key]["next"] = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.data.keys():
            # 获取对应的值
            res = self.data[key]["value"]
            self._refacotr(key)
            return res
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if key in self.data.keys():
            self.data[key]["value"] = value
            self._refacotr(key)
        else:
            if self.capacity > 1:
                if len(self.data) >= self.capacity:
                    # 淘汰
                    first = self._next_key(self.head)
                    self._next_value(self.head)["last"] = None
                    del self.data[self.head]
                    self.head = first

                self.data[key] = {
                    "value": value,
                    "last": self.final,
                    "next": None
                }

                if self.head is None:
                    self.head = key

                if self.final is not None:
                    self._last_value(key)["next"] = key

                self.final = key
            else:
                if self.head is not None:
                    del self.data[self.head]
                self.data[key] = {
                    "value": value,
                    "last": None,
                    "next": None
                }
                self.head = key
                self.final = key


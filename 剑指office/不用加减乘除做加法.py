"""
题目描述
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
"""


# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        # 由于题目要求不能使用四则运算，那么就需要考虑使用位运算
        # 两个数相加可以看成两个数的每个位先相加，但不进位，然后在加上进位的数值
        # 如12+8可以看成2+8=0，由于2+8有进位，所以结果就是10+10=20
        # 二进制中可以表示为1000+1100 先每个位置相加不进位，
        # 则0+0=0 0+1=1 1+0=1 1+1=0这个就是按位异或运算
        # 对于1+1出现进位，我们可以使用按位与运算然后在将结果左移一位
        # 最后将上面两步的结果相加，相加的时候依然要考虑进位的情况，直到不产生进位
        # 注意python没有无符号右移操作，所以需要越界检查
        # 按位与运算：相同位的两个数字都为1，则为1；若有一个不为1，则为0。
        # 按位异或运算：相同位不同则为1，相同则为0。
        while num2 != 0:
            sums = (num1 ^ num2) & 0xffffffff
            carry = (num1 & num2) << 1 & 0xffffffff
            num1 = sums
            num2 = carry
        if num1 <= 0x7fffffff:
            return num1
        else:
            num1 = ~(num1 ^ 0xffffffff)
            return num1


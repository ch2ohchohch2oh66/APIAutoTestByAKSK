# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2024/10/11
# Description: Keep Hungry Keep Foolish
import pytest


def test_start():
    pytest.main(['-v', '-s', './cases'])


if '__main__' == __name__:
    test_start()

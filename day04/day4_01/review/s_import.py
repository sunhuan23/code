# 方式一：
import study_import as s
s.func1(1,3)
s.func2(2,3)

# 方式二：
from study_import import *
func1(1,2)
# func2(1,2)

from study_import import func1 as f
f(4,4)

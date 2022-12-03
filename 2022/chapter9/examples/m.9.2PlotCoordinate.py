import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
plt.plot([1,2,4], [1,2,3])
plt.title("坐标系标题")
plt.xlabel('时间 (s)')
plt.ylabel('范围 (m)')
# $的时候，matplotlib会使用其内置latex引擎绘制数学公式
plt.xticks([1,2,3,4,5],[r'$\pi/3$', r'$2\pi/3$', r'$\pi$',\
                   r'$4\pi/3$', r'$5\pi/3$'])
plt.show()
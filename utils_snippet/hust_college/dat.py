# -*- coding: utf-8 -*-
s = '''
                	  <li><a target="_blank" href="http://mse.hust.edu.cn/">机械科学与工程学院</a></li>
                    <li><a target="_blank" href="http://www.cs.hust.edu.cn/">计算机科学与技术学院</a></li>
                    <li><a target="_blank" href="http://life.hust.edu.cn/">生命科学与技术学院</a></li>
                    <li class="blue"><a target="_blank" href="http://ceee.hust.edu.cn/">电气与电子工程学院</a></li>
                    <li class="blue"><a target="_blank" href="http://mat.hust.edu.cn/">材料科学与工程学院</a></li>
                    <li class="blue"><a target="_blank" href="http://ch.hust.edu.cn/">船舶与海洋工程学院</a></li>
                    <li><a target="_blank" href="http://energy.hust.edu.cn/">能源与动力工程学院</a></li>
                    <li><a target="_blank" href="http://auto.hust.edu.cn/">自动化学院</a></li>
                    <li><a target="_blank" href="http://oei.hust.edu.cn">光学与电子信息学院</a></li>
                    <li class="blue"><a target="_blank" href="http://hae.hust.edu.cn/">水电与数字化工程学院</a></li>
                    <li class="blue"><a target="_blank" href="http://sse.hust.edu.cn/">软件学院</a></li>
                    <li class="blue"><a target="_blank" href="http://ese.hust.edu.cn/">环境科学与工程学院</a></li>
                    <li><a target="_blank" href="http://ei.hust.edu.cn/">电子与信息工程系</a></li>
                    <li><a target="_blank" href="http://aup.hust.edu.cn/">建筑与城市规划学院</a></li>
                    <li><a target="_blank" href="http://civil.hust.edu.cn/">土木工程与力学学院</a></li>
                    <li class="blue"><a target="_blank" href="http://chem.hust.edu.cn/">化学与化工学院</a></li>
                    <li class="blue"><a target="_blank" href="http://maths.hust.edu.cn/new/index.asp">数学与统计学院</a></li>
                   <li class="blue"><a target="_blank" href="http://phys.hust.edu.cn/">物理学院</a></li>
                    <li><a target="_blank" href="http://spa.hust.edu.cn/2008/">公共管理学院</a></li>
                    <li><a target="_blank" href="http://eco.hust.edu.cn/">经济学院</a></li>
                    <li><a target="_blank" href="http://cm.hust.edu.cn/">管理学院</a></li>
                    <li class="blue"><a target="_blank" href="http://humanity.hust.edu.cn/">人文学院</a></li>
                    <li class="blue"><a target="_blank" href="http://phil.hust.edu.cn/">哲学系</a></li>
                    <li class="blue"><a target="_blank" href="http://chinese.hust.edu.cn/">中文系</a></li>
                    <li><a target="_blank" href="http://sjic.hust.edu.cn">新闻与信息传播学院</a></li>
                    <li><a target="_blank" href="http://politics.hust.edu.cn/">马克思主义学院</a></li>
                    <li><a target="_blank" href="http://soci.hust.edu.cn/">社会学系</a></li>
                    <li class="blue"><a href="http://law.hust.edu.cn/Index.asp" target="_blank" class="setting">法学院</a></li>
                    <li class="blue"><a target="_blank" href="http://fld.hust.edu.cn/">外国语学院</a></li>
                    <li class="blue"><a target="_blank" href="http://202.114.128.25/jcyxy/">基础医学院</a></li>
                    <li><a target="_blank" href="http://yxy.tjmu.edu.cn/">药学院</a></li>
                    <li><a href="http://mms.tjmu.edu.cn/" target="_blank">医药卫生管理学院</a></li>
                    <li><a target="_blank" href="http://gwxy.tjmu.edu.cn/">公共卫生学院</a></li>
                    <li class="blue"><a target="_blank" href="http://202.114.128.250/fayixi/">法医学系</a></li>
                    <li class="blue"><a target="_blank" href="http://202.114.128.250/huli/">护理学系</a></li>
                    <li class="blue"><a target="_blank" href="http://www.reprodcentre.com/">计划生育研究所</a></li>
                    <li><a target="_blank" href="http://www.whuh.com/">第一临床学院</a></li>
                    <li><a target="_blank" href="http://www.tjh.com.cn/">第二临床学院</a></li>
                    <li><a target="_blank" href="http://www.liyuanhospital.com/">第三临床学院</a></li>
                    <li class="blue"><a target="_blank" href="http://art.hust.edu.cn/">大学生艺术团</a></li>
                    <li class="blue"><a target="_blank" href="http://www2.hust.edu.cn/jky/">教育科学研究院</a></li>
                    <li class="blue"><a target="_blank" href="http://sie.hust.edu.cn/">国际教育学院</a></li>
                    <li><a target="_blank" href="http://history.hust.edu.cn/">历史研究所</a></li>
                    <li><a target="_blank" href="http://guoxue.hust.edu.cn/">国学研究院</a></li>
                    <li><a target="_blank" href="http://pe.hust.edu.cn/">体育部</a></li>
                    <li class="blue"><a target="_blank" href="http://icare.hust.edu.cn/">中欧清洁与可再生能源学院</a></li>
                    <li class="blue"><a target="_blank" href="http://www.hust-snde.com/">远程与继续教育学院</a></li>
                    '''
import re
import pprint
for i in re.findall('<li.*>(.*)</a></li>', s):
  print '<option value="%s">%s</option>' % (i, i)

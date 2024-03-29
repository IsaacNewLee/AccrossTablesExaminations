# _*_ coding=utf-8 _*_

import pymysql


conn = pymysql.connect(host='localhost',user='root',password='123',database='db7')

# 1、查询所有的课程的名称以及对应的任课老师姓名
sql1 = """
        select course.cname,teacher.tname from course 
            inner join teacher
            on course.teacher_id=teacher.tid
        ;  
    """
# 2、查询学生表中男女生各有多少人
sql2 = """
        select gender,count(gender) from student group by gender;
    """
# 3、查询物理成绩等于100的学生的姓名
sql3 = """
        select sname from student where sid in (
            select student_id from score where num=100 and course_id=
            (
                select cid from course where cname='物理'
            )
        );
    """
# 4、查询平均成绩大于八十分的同学的姓名和平均成绩
sql4 = """
        select sname,t1.avg_score from student inner join (
            select student_id, avg(num) as avg_score from score
            group by student_id
            having avg(num)>80
        ) as t1
        on t1.student_id=student.sid
        ;
    """
# 5、查询所有学生的学号，姓名，选课数，总成绩

# 6、 查询姓李老师的个数

# 7、 查询没有报李平老师课的学生姓名

# 8、 查询物理课程比生物课程高的学生的学号

# 9、 查询没有同时选修物理课程和体育课程的学生姓名

# 10、查询挂科超过两门(包括两门)的学生姓名和班级

# 11查询选修了所有课程的学生姓名


# 12、查询李平老师教的课程的所有成绩记录


# 13、查询全部学生都选修了的课程号和课程名


# 14、查询每门课程被选修的次数


# 15、查询之选修了一门课程的学生姓名和学号


# 16、查询所有学生考出的成绩并按从高到低排序（成绩去重）


# 17、查询平均成绩大于85的学生姓名和平均成绩


# 18、查询生物成绩不及格的学生姓名和对应生物分数


# 19、查询在所有选修了李平老师课程的学生中，这些课程(李平老师的课程，不是所有课程)平均成绩最高的学生姓名


# 20、查询每门课程成绩最好的前两名学生姓名


# 21、查询不同课程但成绩相同的学号，课程号，成绩


# 22、查询没学过“叶平”老师课程的学生姓名以及选修的课程名称；


# 23、查询所有选修了学号为1的同学选修过的一门或者多门课程的同学学号和姓名；


# 24、任课最多的老师中学生单科成绩最高的学生姓名

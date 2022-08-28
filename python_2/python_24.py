'''
    mysql zip安装
        建立文件my.ini内容在下方
        cmd中打开管理员模式
        cd寻找相应的文件
        初始化获得初始密码：mysqld --defaults-file=D:\mysql-8.0.28-winx64\my.ini--initialize console
        安装 mysqld install +相应的程序名字
        环境变量中Path加入相应的文件夹
        用来登录mysql: mysql -uroot -p;  必须要加;
        Enter password:直接空格就可以，或者输入初始化获得的密码，或者改了之后的密码
        修改初始化密码：alter user 'root'@'localhost' identified with mysql_native_password by'123456'; 必须要加;
        show databases；用来展示当前mysql所有的数据库

    任务处理器=>服务=>MYSQL和MYSQL80只能同时运行一个


'''
'''
    Dos命令，打开cmd
        输入net start 查看服务状态
        net  
        net stop MySQL80  关闭服务
        net strat MySQL80  关闭服务
    计算机服务=>管理=>服务和应用程序->服务
    
    quit\exit  退出
        
    mysql -h 127.0.0.1 -uroot -p    dos用cmd中调用服务
    
    
'''
'''
my.ini 内容:

[mysql d]
#设置3306端口
port=3306
#设置mysql的安装目录
basedir=D:\\mysql-8.0.28-winx64
#设置mysql数据库的数据的存放目录
datadir=D:\\mysql-8.0.28-winx64\\data
#允许最大连接数
max_connections=200
#允许连接失败的次数。这是为了防止有人从该主机试图攻击数据库系统
max_connect_errors=10
#服务端使用的字符集默认为UTF8
character-set-server=utf8
#创建新表时将使用的默认存储引擎
default-storage-engine=INNODB
#默认使用“mysql_native_password”插件认证
default_authentication_plugin=mysql_native_password

[mysql]
#设置mysql客户端默认字符集
default-character-set=utf8

[client]
#设置mysql客户端连接服务端时默认使用的端口
port=3306
default-character-set=utf8
'''
'''
    数据类型：指创建表是给数据指定的类型
        常用：
         数值类型：
            整数 int 4个字节 int(m)
                 bigint 8个字节
            浮点数：
                单精度 float 4个字节
                双精度 double 8个字节 double(m,d) 四舍五入
            定点数：
                存储更加精确，一般用于￥
                decimal(m,d) 相似浮点数，默认decimal(10,0)
         字符串类型：
            char 数据量较少，身份证手机号   固定长度 范围0~255    char(m):补充0，满足m个字符
            varchar 数据量较少，邮箱QQ  可变长度 范围0~65535  varchar(m)：不补充
            text 数据数量大的文本数据，文章小说
            blob 数据数量大的二进制数据，图片视频 
         日期时间类型
            data 存储（年月日）
            datatime (年月日，时分秒),范围更大
            timestamp (年月日，时分秒)
            year (年)
            time （时分秒）
         json数据类型
            json是一种轻量级的数据交换格式，类似于XML，但更简单易读好编写
            json分类：json数组和json对象
                json数组 可存储多种类型[值1,值2,值3,......]
                json对象 {"键1":值1,"键2":值2,"键3":值3,......}
                
                    
                        
'''
'''
sql语句_数据库：
    创建数据库test:
        create database test;
    查看数据库：
        show databases;
    查看test数据库的创建信息
        show create database test;
    修改test数据库的编码utf8为gbk
        alter database test character set gbk;
    删除数据库test
        drop database test

sql语句_表:
        创建表student：
            create table(
                id int(6),
                name varchar(20),
                age int(3)
            );
        查看表student
            desc student;
        查看表student详细内容
            show create table student; 
        修改表名
            alter table student rename stu;
        --修改字段数据类型
            desc stu;
            alter table stu modify weight float(10);
        --修改多个字段的数据类型
            alter table stu modify weight double(2,2),
                            modify age int(2);
        --修改数据名和类型
            alter table stu change age old int(3);
        --末尾，首部，任意字段后，添加新字段score以及数据类型
            alter table stu add score int(2);
            alter table stu add score1 int(2) first;
            alter table stu add score2 int(2) after score1;
        --删除字段
            alter table stu drop score2;
        --删除表
            drop table test;
完整性约束
        primary key 主键约束
        unique  唯一约束
        not null    非空约束
        default 默认约束
        auto_increment  自动增加约束
        foreign key 外键约束
        增加约束：
        例如：添加primary key：
             create table student(
             id int(8) primary key,
             name varchar(20),
             age int(2),
             sex varchar(1)
             );
             或者
             create table student1(
             id int(8) ,
             name varchar(20),
             age int(2),
             sex varchar(1),
             constraint student1 primary key(id)
             );
             或者
             create table student2(
             id int(8) ,
             name varchar(20),
             age int(2),
             sex varchar(1),
             constraint student2 primary key(id,name)
             );
        给已有的表添加主键，只能在空白约束的表操作
            create table student3(
                 id int(8) ,
                 sex varchar(1)
            );
            --添加约束
            alter table student3 add constraint student3 primary key(sex);
            --删除约束，不同约束的删除(drop)，修改(modify)，添加(add)方法不同
            alter table student3 drop primary key;
        唯一约束：
            唯一
            create table student4(
            id int(8) primary key,
            name varchar(20) unique,
            age int(2),
            sex varchar(1)
            );
            desc student4;
        非空约束，默认约束
            非空，一般在已有表修改
            create table student5(
                id int(8) primary key,
                name varchar(20) unique,
                age int(2) not null,
                sex varchar(1)
            );
            desc student5;
            默认
            create table student6(
            id int(8) primary key,
            name varchar(20) unique,
            age int(2) not null,
            sex varchar(1) default'男'
            );
            desc student6;
        自动增长约束
            自动增长，用于int,配合主键使用
            create table student7(
            id int(8) primary key auto_increment,
            name varchar(20) unique,
            age int(2) not null,
            sex varchar(1) default'男'
            );
            desc student7;
        外键约束
            外键
            create table student8(
            id int(8) primary key auto_increment,
            name varchar(20) unique
            );
            create table student8_0(
            id int(8) primary key auto_increment,
            name varchar(20) unique,
            stu_id int(8),
            constraint student8_0_stu_id foreign key(stu_id) references student8(id)
            )
            
            
        

             
             

        
'''
'''
    自动查询表index_student中的索引
    create table index_student(
        sno int(4)primary key auto_increment,
        sname varchar(20) unique,
        age int(2)
    );
    desc index_student;
    show index from index_student;
    
    手动索引
    创建普通索引
        create table index_student1(
            sno int(4),
            sname varchar(20),
            age int(2),
            index(sno)
        )
    查看添加的索引
        show index from index_student1;
    创建唯一索引
        create table index_student2(
        sno int(4),
        sname varchar(20),
        age int(2),
        unique index(sno)
        );
        show index from index_student2;
    创建主键索引
        create table index_student3(
        sno int(4),
        sname varchar(20),
        age int(2),
        primary key (sno)
        );
        show index from index_student3;
    创建全文索引（只能用于字符串）
        create table index_student4(
        sno int(4),
        sname varchar(20),
        age int(2),
        fulltext index (sno)
        );
        show index from index_student4;
    创建空间索引（只能用于空间数据类型）
        create table index_student5(
        sno int(4),
        sname varchar(20),
        age int(2),
        sloc point not null,
        spatial index (sloc)
        );
        show index from index_student5;
    创建复合索引
        create table index_student6(
        sno int(4),
        sname varchar(20),
        age int(2),
        index (sno,sname)
        );
        show index from index_student6;
        
        
    表已经存在，创建索引,不能添加主键索引key
        create table index_student7(
        sno int(4),
        sname varchar(20),
        age int(2),
        sinfo varchar(100),
        sloc point not null
        );
        普通索引
        create index index_student7_sno on index_student7(sno);
        show index from index_student7;
        唯一索引
        create unique index index_student7_sname on index_student7(sname);
        show index from index_student7;
        全文索引
        create fulltext index index_student7_sinfo on index_student7(sinfo);
        show index from index_student7;
        空间索引
        create spatial index index_student7_sloc on index_student7(sloc);
        show index from index_student7;
        复合索引
        create  index index_student7_sno_sname on index_student7(sno,sname);
        show index from index_student7;
    
    
    
    --已有表添加索引
            create table index_student8(
                sno int(8),
                sname varchar(20),
                age int(2),
                sloc point not null
            );
        --删除
            drop table index_student8;
        --展示索引
            show index from index_student8; 
        --普通索引
            alter table index_student8
                add index(sno)
        --唯一索引
            alter table index_student8
                add unique index(sname);
        --主键索引
            alter table index_student8
                add primary key (sno);
        --全文索引
            alter table index_student8
                add fulltext (sname);
        --空间索引
            alter table index_student8
                add spatial (sloc);
        --复合索引
            alter table index_student8
                add	index (sno,sname);
                
        --删除索引，主键索引使用其他方法
        alter table index_student8 drop index  sno;
        或者
        drop index sloc on index_student8;
        
        

'''
'''
    --插入数据
        create table student8(
            sno int(8) primary key,
            sname varchar(10) not null,
            age int(2),
            sex varchar(5) default'man',
            email varchar(30) unique
        );
        create table student8_test(
            sno int(8) primary key,
            sname varchar(10) not null,
            age int(2),
            sex varchar(5) default'man',
            email varchar(30) unique
        );
        --展示字段数据
        select * from student8;
        select * from student8_test;
        --所有字段插入数据
        insert into student8(sno,sname,age,sex,email)
                        value(1,'收到',34,'women','@qq.com');
        insert into student8 values(2,'可能',84,'men','@163.com')
        --指定字段
        insert into student8(sno,sname)
                        value(3,'IC');
        --set方式插入
        insert into student8 set sno=5,sname='博人',age=19,email='@phone.com';
        --同时插入多条数据
        insert into student8(sno,sname,age,sex,email)
                        value(4,'发表',02,'women','@7k7k.com'),
                                    (6,'方式',23,'men','@4399.com'),
                                    (7,'欧文',32,'women','@blilblil.com');
        --插入查询结果
        insert into student8_test select * from student8;
        
    --更新数据
        --更新指定数据
        update student8 set sname='阿斯顿' where sname='收到';
        --更新全部数据
        update student8 set sex='women';
    --删除数据
        --指定
        delete  from student8 where sno>6;
        --全部
        delete  from student8;
        --truncate 关键字删除
        truncate student8;
DML数据操纵语言，DDL数据定义语言
    
    
'''
'''
    create table emp(
        empno int(4) primary key,
        emame varchar(10),
        job varchar(9),
        mgr int(4),
        hiredata date,
        sal decimal(7,2),
        comm decimal(7,2),
        deptno int(2)
        
    );
    insert into emp values
    ( 7369,'Smith','clerk',7902,'1980-12-17',800,null,20),
    (7499,'Allen','salesman',7698,'1981-02-20',1600,300,30),
    (7521,'ward','salesman',7698,'1981-02-22',1250,58,30),
    (7566,'Janes','manager',7839,'1981-04-02',2975,null,20),
    (7654,'Maritn','salesman',7698,'1981-09-28',1250,1408,30),
    (7698,'Blake', 'manager',7839,'1981-05-01',2850,null,30),
    (7782,'Clark','manager',7839,'1981-06-09',2450,null,10),
    (7788,'Scott','analyst',7566,'1987-04-19',3000,null,20);
    insert into emp values
    (7789,'Scott','analyst',7567,'1987-03-19',3000,null,20);
     
    
    --查询字段
    select * from emp;
    或者
    select emame,empno,job,mgr,hiredata date,sal,deptno from emp;
    --去重复
    select distinct deptno,emame from emp;
    --算术运算符+ - * /(div) %
    select deptno*3 from emp;
    --字段取别名
    select sal*12 as 'yearsal&年薪' from emp;
    
    --查询结果排序，默认升序
    --单个字段
    select * from emp order by sal asc;
    --多个字段,asc升序,desc降序
    select *from emp order by sal asc,empno desc;
    --条件查询,><=!,不区分大小写
    select * from emp where sal=3000;
    select * from emp where job='analyst';
    --binary,区分大小写
    select * from emp where binary job='ANALYST';
    select * from emp where binary job='analyst';
    --查询区间范围，包括边界
    select * from emp where sal between 2000 and 3000;
    select * from emp where sal not between 2000 and 3000;
    --查询指定集合
    select * from emp where sal in(800,3000);
    select * from emp where sal not in(800,3000);
    --查看字段是否为空
    select *from emp where comm is not null;
    select *from emp where comm is null;
    --模糊查询 %开头结尾中间 _相当于代替一个空字符,可与%混用
    select * from emp where emame like 's%';
    select * from emp where emame like '%s';
    select * from emp where emame like '%s%';
    select * from emp where emame like '%_____';
    select * from emp where emame like '_a%';
    --逻辑运算符 and or 
    select * from emp where deptno=20 or sal>=2000;
    select * from emp where deptno=20 and sal>=2000;
    --select 查询内容|from 表名|where 条件|order by 字段 asc、desc 升序、降序|limit a,b 从第a条，显示b条数据
    --分页查询，与排序连用时，先排序
    select * from emp limit 0,4;
    select * from emp limit 4,2;

'''
'''
    create table emp(
        empno int(4) primary key,
        ename varchar(10),
        job varchar(9),
        mgr int(4),
        hiredata date,
        sal decimal(7,2),
        comm decimal(7,2),
        deptno int(2)
    );
    insert into emp values
    ( 7369,'Smith','clerk',7902,'1980-12-17',800,null,20),
    (7499,'Allen','salesman',7698,'1981-02-20',1600,300,30),
    (7521,'ward','salesman',7698,'1981-02-22',1250,58,30),
    (7566,'Janes','manager',7839,'1981-04-02',2975,null,20),
    (7654,'Maritn','salesman',7698,'1981-09-28',1250,1408,30),
    (7698,'Blake', 'manager',7839,'1981-05-01',2850,null,30),
    (7782,'Clark','manager',7839,'1981-06-09',2450,null,10),
    (7788,'Scott','analyst',7566,'1987-04-19',3000,null,20),
    (7789,'Scott','analyst',7567,'1987-03-19',3000,null,20);
     
select * from emp;
--字符函数
    --拼接字符串
    select concat('雇员姓名:',ename,'薪资',sal,'职位',job,'入职日期',hiredata,'年薪',sal*13) from emp;
    --查询字段长度
    select * from emp where length('ename')=5;
    --转换大小写
    select ename,upper('ename'),lower('ename') from emp;
    --指定字符串中,将特定字段替换新字段
    create table emp1(
    name1 varchar(20),
    age int(2),
    sex varchar(9)
    );
    insert into emp1 values(
    'tom',3,'man'
    );
    select * from emp1;
    select replace('tom','m','m&jary') from emp1;
    --截取指定字符串,选择截取的片段
    select substring(ename,2,4) from emp;
    
--数值函数
    --绝对值
    select abs(-3),abs(3);
    --派,3.14....
    select pi();
    --取余数
    select mod(7,3);
    --次方
    select pow(3,4);
    --向上取整，向下取整
    select ceil(3.533),floor(11.334);
    --四舍五入
    select round(23.4466),round(2.23215,3);
    --截取小数
    select truncate(23.3423,0),truncate(23.3423,2);
    --浮点类型随机数
    select rand(0),rand(1);
    --获取时间
    select now(),curdate(),curtime(),sleep(2),sysdate();
    --休息2s
    select sleep(2);
    --获取当前年份的第几天，第几周
    select dayofyear(now()),week(now());
    --计算两个日期的时间间隔
    select datediff('2008-1-1',now());
    --日期的加减
    select date_add(now(),interval '5' day),date_sub(now(),interval '2_3' year_month);
    
--流程控制函数
    --if条件
    select if(1>5,'1','5');
    select sal,if(sal>2000,'高','低') from emp;
    --ifnull,替换null
    select sal,comm,(sal+ifnull(comm,0)) from emp;
    --nullif 判断两个值是否相等
    select nullif(1,2),nullif(1,1);
    --case并列条件
    select deptno,sal,ename,
        case 
        when deptno=10 then '部门1'
        when deptno=20 then '部门2'
        else '部门3'
        end
    from emp;   
        
    select * from emp;
--多行函数（分组函数）
    --count统计记录的数目
    select count(*) from emp; 
    --计算非空数目
    select count(comm) from emp;
    --计算不重复且非空
    select count(distinct(mgr))from emp;
    select count(distinct(ifnull(mgr,1)))from emp;
    --sum求和
    select sum(sal) from emp;
    --去掉重复
    select sum(distinct(sal)) from emp;
    --avg平均值
    select avg(sal) from emp;
    --max最大值，min最小值
    select max(sal),min(sal) from emp;
        
--分组统计
    select deptno,count(*) from emp group by deptno;
    select deptno,avg(sal) from emp group by deptno;
    select deptno,max(sal),min(sal),count(*) from emp group by deptno;
    select job,count(*) from emp group by job;
    --分组函数条件表达
    select deptno,count(*) from emp group by deptno having count(*)>2;
    select sal,job from emp group by empno,job having avg(sal)>1000;
    
--多表查询
    create table dept(
        deptno int(6) primary key,
        dname varchar(20),
        loc varchar(20)
    );
    insert into dept values
        (10,'accounting','new york'),
        (20,'research','dallas'),
        (30,'sales','chicago'),
        (40,'operations','boston');
    select * from dept;
    select count(*) from dept;
    create table emp1(
        empno int(4) primary key,
        job varchar(20),
        ename varchar(20),
        mgr int(4),
        hiredata date,
        sal decimal(8,2),
        com decimal(8,2),
        deptno int(4),
        constraint emp1_deptno foreign key(deptno) references dept(deptno)
    );
    insert into emp1 values
        (7499,'Allen','salesman',7698,'1981-02-20',1609,300,30),
        (7521,'Ward','salesman',7698,'1981-02-22',1250,500,30),
        (756,'Jones','manager',7839,'1981-04-02',2975,null,20),
        (7654,'Haritn','salesman', 7698,'1981-09-28',1258,1480,30),
        (7698,'Blake','manager',7839,'1981-05-01',2850,null,30),
        (7782,'clark','manager', 7839,'1981-06-09',2450,null,10),
        (7788,'Scott ','analyst',7566,'1987-04-19',3000,null, 20),
        (7839,'King','president',null,'1981-11-17',5800,null, 10),
        (7844,'Turner','salesman',7698,'1981-09-08',1500,8,30),
        (7876,'Adams','clerk',7788,'1987-05-23',1100, null, 20),
        (7908,'James','clerk',7698,'1981-12-03',950,null,30),
        (7902,'Ford','analyst', 7566,'1981-12-03',1200,null,20),
        (7934,'Hilier','clerk',7782,'1982-01-23',1308,null,10);
    select * from emp1;
    select count(*) from emp1;
        
--交叉连接
    select * from emp1 cross join dept; 
    select count(*) from emp1;
    select count(*) from dept;
    select count(*) from emp1 cross join dept;
--自然连接
    select * from emp1 natural join dept;
    select count(*) from emp1 natural join dept;
    --内连接
    select * from emp1,dept where emp1.deptno=dept.deptno;
    select * from emp1 e,dept d where e.deptno=d.deptno;
    或者
    select *from emp1 inner join dept on emp1.deptno=dept.deptno;
    select *from emp1 inner join dept where emp1.deptno=dept.deptno;
    select emp1.ename,dept.* from emp1 inner join dept on emp1.deptno=dept.deptno where emp1.deptno=20;
    --自连接
    select * from emp1 e,emp1 m where e.mgr=m.empno;
    select *from emp1 e,emp1 m where e.mgr=m.empno and e.empno>m.empno;
    或者
    select *from emp1 e join emp1 m where e.mgr=m.empno;
    select *from emp1 e join emp1 m where e.mgr=m.empno and e.empno>m.empno;
    select *from emp1 e join emp1 m on e.mgr=m.empno where e.empno>m.empno;
    --外连接，显示不满足条件的信息
    select * from emp1 e,emp1 m where e.mgr=m.empno;
    --左外连接，左右取决于两个表放的位置
    select * from dept d left outer join emp1 e on e.deptno=d.deptno;  
    --右外连接
    select * from emp1 e right outer join dept d on e.deptno=d.deptno; 
--子查询作为条件
    --标量子查询，查询嵌套
    select * from emp1 where sal<(select sal from emp1 where job='King');
    --行子查询,返回多列数据
    select * from emp1 where (deptno,ename)=(select deptno,ename from emp1 where job='Allen')
    --列子查询，返回多行数据,不能用<>=!,in\any\all\exists
    select * from emp1 where ename in(select ename from emp1 where deptno=10) and deptno=20;
    select * from emp1 where sal<any(select sal from emp1 where ename='clerk');
    select * from emp1 where sal>all(select sal from emp1 where ename='clerk');
    select * from dept where exists(select * from emp1 where emp1.deptno=dept.deptno);
--子查询作为表，需要自己命名这个表名字
    select max(avgsal)from(select avg(sal) avgsal from emp1 group by deptno) avg_sal;
    select * from dept d,(select count(*) cou,deptno from emp1 group by deptno) dd where d.deptno=dd.deptno;
    或者
    select * from dept d inner join (select count(*) cou,deptno from emp1 group by deptno) dd where d.deptno=dd.deptno;
        
'''
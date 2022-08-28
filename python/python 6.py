#分数评分等级
score=int(input("请输入分数："))
grade='ABCDE'
num=score
a,b,c=1,2,3
if (score > 100 or score < 0):
    print('数据错误')
else:
    if score >=60 :#嵌套的第二个if，不能用or形式的范围
        if score ==100:
            print('great!')
        else:
            num=score//10
            print("分数={0},等级={1}".format(score,grade[9-num]))
    else:
        print("分数={0},等级={1}".format(score, grade[4]))




from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px

import csv, re, operator
# from textblob import TextBlob

app = Flask(__name__)

person = {
    'first_name': 'zhou',
    'last_name' : 'mingtao',
    'name' :'Zhou Mingtao' ,
    'address' : '湖北孝感',
    'job': '无',
    'PersonalElucidation': '知道的越多，不知道的也越多',
    'tel': '+86 15586537731',
    'email': 'zhou1749957042@gmail.com',
    'web':"www.baidu.com",
    'description' : '加油！',
    'social_media' : [
        {
            'link': 'https://gitee.com/zhou-mingtao',
            'icon' : 'fa-facebook-f'
        },
        {
            'link': 'https://github.com/1749957042',
            'icon' : 'fa-github'
        },
        {
            'link': 'linkedin.com/in/nono',
            'icon' : 'fa-linkedin-in'
        },
        {
            'link': 'https://blog.csdn.net/qq_44250569?spm=1001.2014.3001.5343',
            'icon' : 'fa-twitter'
        }
    ],
    'img': 'img/img_nono.jpg',
    'experiences' : [
        {
            'title' : '教育经历',
            'company': '湖北师范大学',
            'description' : '无',
            'timeframe' : '2018.9-2020.6'
        },
        {
            'title' : '启明普法项目',
            'company': '项目经历',
            'description' : '一个 基于SSM框架搭建的新闻类网站，登录后的用户可通过趣味答题来了解一些基本的法律法规',
            'timeframe' : '2020.10 - 2021.01'
        },
        {
            'title' : '谷粒商城',
            'company': '项目经历',
            'description' : '谷粒商城后台管理系统是一套B2C模式电商系统,销售自营给客户，基于SpringBoot+MyBatis实现。',
            'timeframe' : '2021.2 - 2021.5'
        }
    ],
    'education' : [
        {
            'university': 'Paris Diderot',
            'degree': 'Projets informatiques et Startégies d\'entreprise (PISE)',
            'description' : 'Gestion de projets IT, Audit, Programmation',
            'mention' : 'Bien',
            'timeframe' : '2015 - 2016'
        },
        {
            'university': 'Paris Dauphine',
            'degree': 'Master en Management global',
            'description' : 'Fonctions supports (Marketing, Finance, Ressources Humaines, Comptabilité)',
            'mention' : 'Bien',
            'timeframe' : '2015'
        },
        {
            'university': 'Lycée Turgot - Paris Sorbonne',
            'degree': 'CPGE Economie & Gestion',
            'description' : 'Préparation au concours de l\'ENS Cachan, section Economie',
            'mention' : 'N/A',
            'timeframe' : '2010 - 2012'
        }
    ],
    'programming_languages' : {
        'HTML' : ['fa-html5', '100'],
        'CSS' : ['fa-css3-alt', '100'], 
        'SASS' : ['fa-sass', '90'], 
        'JS' : ['fa-js-square', '90'],
        'Wordpress' : ['fa-wordpress', '80'],
        'Python': ['fa-python', '70'],
        'Mongo DB' : ['fa-database', '60'],
        'MySQL' : ['fa-database', '60'],
        'NodeJS' : ['fa-node-js', '50']
    },
    'languages' : {'英语' : 'Professional','Chinese' : 'Professional'},
    'interests' : ['PingPong', 'Game', 'Programming','listen']
}

@app.route('/')
def cv(person=person):
    return render_template('index.html', person=person)




@app.route('/callback', methods=['POST', 'GET'])
def cb():
	return gm(request.args.get('data'))

def cb1():
 	return gm1(request.args.get('data'))
def cb2():
 	return gm2(request.args.get('data'))
def cb3():
 	return gm3(request.args.get('data'))
   
@app.route('/chart')
def chart():
	return render_template('chartsajax.html',  graphJSON=gm() , graphJSON1=gm1() , graphJSON2=gm2() , graphJSON3=gm3() ,
                                               graphJSON4=gm4() , graphJSON5=gm5() , graphJSON6=gm6() , graphJSON7=gm7(),
                                               graphJSON8=gm8() , graphJSON9=gm9() , graphJSON10=gm10() , graphJSON11=gm11()
						                       )
#线条图
def gm(sex='Female'):
	df = pd.read_csv(r'static/tips.csv')

	fig = px.line(df[df['sex']==sex], x="tip", y="size", color = "day")

	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

#条形图
def gm1(sex='Female'):
	df = pd.read_csv(r'static/tips.csv')

	fig = px.bar(df[df['sex']==sex], x="total_bill", y="size", color = "day")

	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

#散点图
def gm2(sex='Female'):
	df = pd.read_csv(r'static/tips.csv')

	fig = px.scatter(df[df['sex']==sex], x="tip", y="size")

	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

#矩阵散点图
def gm3(sex='Female'):
	df = px.data.tips()

	fig = px.scatter_matrix(df[df['sex']==sex])

	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

#并行类别图
def gm4(sex='Female'):
	df = pd.read_csv(r'static/tips.csv')

	fig = px.parallel_categories(df[df['sex']==sex],color="size", color_continuous_scale=px.
            colors.sequential.Inferno)

	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON


#堆积区域图
def gm5(sex='Female'):
	df = pd.read_csv(r'static/tips.csv')

	fig = px.area(df[df['sex']==sex],x="tip", y="size", color="time",
        line_group="time")

	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

#密度等值线图
def gm6(sex='Female'):
	df = pd.read_csv(r'static/tips.csv')

	fig = px.density_contour(df[df['sex']==sex], x="tip", y="size")

	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

#条形图，设置堆积类型
def gm7(sex='Female'):
	df = pd.read_csv(r'static/tips.csv')

	fig = px.bar(df[df['sex']==sex], x="sex", y="total_bill", color="smoker", barmode="group")

	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

#直方图，并在上分增加细条图
def gm8(sex='Female'):
	df = pd.read_csv(r'static/tips.csv')

	fig = px.histogram(df[df['sex']==sex], x="total_bill", y="tip", color="sex", marginal="rug",
             hover_data=df[df['sex']==sex].columns)

	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

#长条图，设置方向为水平
def gm9(sex='Female'):
	df = pd.read_csv(r'static/tips.csv')

	fig = px.strip(df[df['sex']==sex], x="total_bill", y="time", orientation="h", color="smoker")

	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

#箱形图，设置使用槽口绘制框
def gm10(sex='Female'):
	df = pd.read_csv(r'static/tips.csv')

	fig = px.box(df[df['sex']==sex], x="day", y="total_bill", color="smoker", notched=True)

	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

#小提琴图，同时在内部显示箱图，展示所有采样数据
def gm11(sex='Female'):
	df = pd.read_csv(r'static/tips.csv')

	fig = px.violin(df[df['sex']==sex], y="tip", x="smoker", color="sex", box=True, points="all",
          hover_data=df[df['sex']==sex].columns)

	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON



@app.route('/senti')
def main():
	text = ""
	values = {"positive": 0, "negative": 0, "neutral": 0}

	with open('ask_politics.csv', 'rt') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
		for idx, row in enumerate(reader):
			if idx > 0 and idx % 2000 == 0:
				break
			if  'text' in row:
				nolinkstext = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', '', row['text'], flags=re.MULTILINE)
				text = nolinkstext

			blob = TextBlob(text)
			for sentence in blob.sentences:
				sentiment_value = sentence.sentiment.polarity
				if sentiment_value >= -0.1 and sentiment_value <= 0.1:
					values['neutral'] += 1
				elif sentiment_value < 0:
					values['negative'] += 1
				elif sentiment_value > 0:
					values['positive'] += 1

	values = sorted(values.items(), key=operator.itemgetter(1))
	top_ten = list(reversed(values))
	if len(top_ten) >= 11:
		top_ten = top_ten[1:11]
	else :
		top_ten = top_ten[0:len(top_ten)]

	top_ten_list_vals = []
	top_ten_list_labels = []
	for language in top_ten:
		top_ten_list_vals.append(language[1])
		top_ten_list_labels.append(language[0])

	graph_values = [{
					'labels': top_ten_list_labels,
					'values': top_ten_list_vals,
					'type': 'pie',
					'insidetextfont': {'color': '#FFFFFF',
										'size': '14',
										},
					'textfont': {'color': '#FFFFFF',
										'size': '14',
								},
					}]

	layout = {'title': '<b>意见挖掘</b>'}

	return render_template('sentiment.html', graph_values=graph_values, layout=layout)


if __name__ == '__main__':
  app.run(debug=True, port=80, host="0.0.0.0", threaded=True)

import re
import requests
key=input("输入你想搜索的领域的岗位信息:")
data={"fromJs":"1",
      "jobarea":"020000",
      "keyword":key,
      "keywordtype":"2",
      "curr_page":"1",
      }
hd={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}
response=requests.get("http://search.51job.com/jobsearch/search_result.php",params=data,headers=hd)
data=bytes(response.text,response.encoding).decode("gbk","ignore")
pat_page="共(.*?)条职位"
allline=re.compile(pat_page,re.S).findall(data)[0]
allpage=int(allline)//50+1
for i in range(0,allpage):
    print("----正在爬"+str(i+1)+"页-----")
    getdata={"fromJs":"1",
      "jobarea":"020000",
      "keyword":key,
      "keywordtype":"2",
      "curr_page":str(i+1),
      }
    response=requests.get("http://search.51job.com/jobsearch/search_result.php",params=getdata,headers=hd)
    thisdata=bytes(response.text,response.encoding).decode("gbk","ignore")
    job_url_pat='<em class="check" name="delivery_em" onclick="checkboxClick.this."></em>.*?href="//jobs.51job.com/(.*?).html'
    job_url_all=re.compile(job_url_pat,re.S).findall(thisdata)[1:]
    for job_url in job_url_all:
        #print(job_url)
        thisurl="http://jobs.51job.com/"+job_url+".html"
        response=requests.get(thisurl)
        thisdata=bytes(response.text,response.encoding).decode("gbk","ignore")
        pat_title='<h1 title="(.*?)"'
        pat_company='<p class="cname">'+'.*?title="(.*?)"'
        pat_money='<div class="tHeader tHjob">.*?<strong>(.*?)</strong>'
        pat_msg='<div class="bmsg job_msg inbox">(.*?)<div class="share">'
        title=re.compile(pat_title,re.S).findall(thisdata)[0]
        company=re.compile(pat_company,re.S).findall(thisdata)[0]
        money=re.compile(pat_money,re.S).findall(thisdata)[0]
        msg=re.compile(pat_msg,re.S).findall(thisdata)[0]
        print("------------")
        print(title)
        print(company)
        print(money)
